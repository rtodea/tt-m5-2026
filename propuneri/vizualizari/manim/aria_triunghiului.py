"""
Aria triunghiului = b * h / 2 — demonstratie animata.

Randare:
    manim -pqh aria_triunghiului.py AriaTriunghiului

Nu foloseste MathTex/Tex nicaieri, deci NU are nevoie de LaTeX instalat.
Daca se instaleaza LaTeX, `Text(...)` se poate inlocui cu `MathTex(...)`
pentru formule mai frumoase.
"""

from manim import *
import numpy as np

AZUR = "#4a7fd0"
CARAMIZIU = "#e07a30"
CARAMIZIU_INCHIS = "#a03000"


class AriaTriunghiului(Scene):
    def construct(self):
        # ---------- configuratia de baza ----------
        A = np.array([-4.0, -2.0, 0.0])
        B = np.array([2.0, -2.0, 0.0])
        C = np.array([0.5, 1.6, 0.0])
        F = np.array([C[0], A[1], 0.0])          # piciorul inaltimii
        sus = np.array([0.0, C[1] - A[1], 0.0])  # vectorul de inaltime

        titlu = Text("Aria triunghiului", font_size=40).to_edge(UP)
        self.play(Write(titlu))

        tri = Polygon(A, B, C, color=CARAMIZIU_INCHIS, stroke_width=4)
        tri.set_fill(CARAMIZIU, opacity=0.35)
        et_a = Text("A", font_size=26).next_to(A, DL, buff=0.15)
        et_b = Text("B", font_size=26).next_to(B, DR, buff=0.15)
        et_c = Text("C", font_size=26).next_to(C, UP, buff=0.15)

        self.play(Create(tri), FadeIn(et_a, et_b, et_c))
        self.wait(0.5)

        # ---------- baza si inaltimea ----------
        baza = Line(A, B, color=AZUR, stroke_width=6)
        et_baza = Text("b", font_size=30, color=AZUR).next_to(baza, DOWN, buff=0.2)
        inaltime = DashedLine(C, F, color=CARAMIZIU_INCHIS, stroke_width=4)
        et_h = Text("h", font_size=30, color=CARAMIZIU_INCHIS).next_to(inaltime, RIGHT, buff=0.15)
        unghi_drept = RightAngle(Line(F, C), Line(F, B), length=0.25,
                                 color=CARAMIZIU_INCHIS)

        self.play(Create(baza), Write(et_baza))
        self.play(Create(inaltime), Write(et_h), Create(unghi_drept))
        self.wait(0.5)

        # ---------- completam la dreptunghi ----------
        drept = Polygon(A, B, B + sus, A + sus, color=AZUR, stroke_width=3)
        drept.set_fill(AZUR, opacity=0.10)
        text_drept = Text("Dreptunghiul are aria  b · h", font_size=30,
                          color=AZUR).to_edge(DOWN)

        self.play(Create(drept), Write(text_drept))
        self.wait(1)

        # ---------- inaltimea taie triunghiul in doua ----------
        stanga = Polygon(A, F, C, color=CARAMIZIU_INCHIS, stroke_width=0)
        stanga.set_fill(CARAMIZIU, opacity=0.55)
        dreapta = Polygon(F, B, C, color=CARAMIZIU_INCHIS, stroke_width=0)
        dreapta.set_fill("#c9622a", opacity=0.55)

        self.play(FadeOut(text_drept))
        self.play(FadeIn(stanga), FadeIn(dreapta))

        text_2 = Text("Înălțimea taie triunghiul în două triunghiuri dreptunghice",
                      font_size=28).to_edge(DOWN)
        self.play(Write(text_2))
        self.wait(1)

        # ---------- fiecare jumatate umple exact jumatate din dreptunghiul ei ----------
        copie_st = stanga.copy()
        copie_dr = dreapta.copy()
        self.add(copie_st, copie_dr)

        mij_AC = (A + C) / 2
        mij_BC = (B + C) / 2

        text_3 = Text("Fiecare jumătate, rotită, umple exact cealaltă jumătate",
                      font_size=28).to_edge(DOWN)
        self.play(ReplacementTransform(text_2, text_3))

        self.play(
            Rotate(copie_st, angle=PI, about_point=mij_AC),
            Rotate(copie_dr, angle=PI, about_point=mij_BC),
            run_time=2.2,
        )
        self.wait(1.2)

        # ---------- concluzia ----------
        concluzie = Text("aria triunghiului  =  b · h : 2", font_size=40,
                         color=CARAMIZIU_INCHIS).to_edge(DOWN)
        self.play(ReplacementTransform(text_3, concluzie))
        self.wait(1.5)

        self.play(FadeOut(copie_st), FadeOut(copie_dr), FadeOut(stanga), FadeOut(dreapta),
                  FadeOut(unghi_drept))

        # ---------- partea a doua: aria nu depinde de unde e varful ----------
        text_4 = Text("Mutăm vârful C pe o paralelă la bază. Ce se schimbă?",
                      font_size=28).to_edge(DOWN)
        self.play(ReplacementTransform(concluzie, text_4))

        ghid = DashedLine(np.array([-6.0, C[1], 0.0]), np.array([6.0, C[1], 0.0]),
                          color=CARAMIZIU, stroke_width=2)
        self.play(Create(ghid))

        x = ValueTracker(C[0])

        def varf():
            return np.array([x.get_value(), C[1], 0.0])

        tri_mobil = always_redraw(
            lambda: Polygon(A, B, varf(), color=CARAMIZIU_INCHIS, stroke_width=4)
            .set_fill(CARAMIZIU, opacity=0.35)
        )
        h_mobila = always_redraw(
            lambda: DashedLine(varf(), np.array([x.get_value(), A[1], 0.0]),
                               color=CARAMIZIU_INCHIS, stroke_width=3)
        )

        self.remove(tri, inaltime, et_c, et_h)
        self.add(tri_mobil, h_mobila)

        self.play(x.animate.set_value(-5.0), run_time=2.5)
        self.play(x.animate.set_value(4.5), run_time=3.5)
        self.play(x.animate.set_value(0.5), run_time=2.0)

        final = Text("b nu s-a schimbat, h nu s-a schimbat  ->  aria nu s-a schimbat",
                     font_size=30, color=CARAMIZIU_INCHIS).to_edge(DOWN)
        self.play(ReplacementTransform(text_4, final))
        self.wait(2.5)
