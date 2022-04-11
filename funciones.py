from manim import *
from manim_fontawesome import Regular, Brand
from manim_revealjs import PresentationScene
from manim_revealjs.plugin import export


MY_GREEN = "#307a2f"
regular = Regular()
brand = Brand()


class Logo(VMobject):
    def __init__(self):
        super().__init__()
        circle = Circle(color=WHITE).set_fill(MY_GREEN, opacity=1)
        tex = MathTex("\\mathrm{H_2O}")
        self.add(circle, tex)


class Thumbnail(Scene):
    def construct(self):
        ax = NumberPlane()
        graph = FunctionGraph(lambda x: x*(x-1)*(x+1)*(x-2), color=RED)
        title = Text("Funciones").scale(2)
        text = Text("¿Qué es una función?").scale(1.5)
        text_group = VGroup(title, text).arrange(DOWN).to_edge(UP)
        rec = SurroundingRectangle(text_group, color=WHITE).set_fill(BLACK, opacity=1)
        eq = MathTex("y", "=", "f", "(", "x", ")").scale(2).to_edge(DOWN)
        eq.set_color_by_tex_to_color_map({"y": BLUE, "f": GREEN, "x": YELLOW})
        emoji = regular.face_surprise.set_color(YELLOW).to_corner(DL)
        logo = Logo().to_corner(DR)
        self.add(ax, graph, rec, text_group, eq, emoji, logo)


class Funciones(PresentationScene):
    def construct(self):
        title = Text("Introducción a las funciones", weight=BOLD)
        logo = Logo()
        text = Text("Pensar para simplificar").scale(0.7)
        group = VGroup(logo, text).arrange(DOWN)
        total_group = VGroup(title, group).arrange(DOWN, buff=1)
        self.add(total_group)
        self.end_fragment()
        self.play(FadeOut(total_group))
        self.end_fragment()


class TableOfContents(PresentationScene):
    def setup(self):
        super().setup()
        titulo = Text("Contenidos del video").to_edge(UP)
        blst = BulletedList(
            "Funciones que quizá ya conocías", "Concepto de función",
            "Ejercicios y problemas de aplicación"
        )
        self.table_of_contents = VGroup(titulo, blst)


class TableOfContents1(TableOfContents):
    def construct(self):
        blst = self.table_of_contents[1]
        self.play(Write(self.table_of_contents))
        self.end_fragment()
        self.play(blst[0].animate.scale(1.2).set_color(YELLOW))
        self.end_fragment()


class Example1(PresentationScene):
    def construct(self):
        title = Text("Funciones que quizá ya conocías").to_edge(UP)
        self.add(title)
        self.end_fragment()

        circle = Circle(radius=2)
        line = Line(ORIGIN, 2*RIGHT)
        center = Dot(color=ORANGE)
        group = VGroup(line, center, circle)

        self.play(Create(group))
        self.end_fragment()

        radius = MathTex("2").set_color(YELLOW)
        radius.next_to(line, UP)
        
        self.play(Write(radius))
        self.end_fragment()

        perimeter = MathTex("P", "=", "2\\pi(", "2\\relax", ")").to_edge(DOWN)
        perimeter.set_color_by_tex_to_color_map({"P": BLUE, "2\\relax": YELLOW})
        
        self.play(Write(perimeter))
        self.end_fragment()

        result = MathTex("P", "=", "4\\pi").to_edge(DOWN)
        result.set_color_by_tex("P", BLUE)

        self.play(ReplacementTransform(perimeter, result))
        self.play(Circumscribe(result))
        self.end_fragment()

        numeric_value = MathTex("P", "\\approx", str(np.round(4 * PI, decimals=4))).next_to(result, UP)
        numeric_value.set_color_by_tex("P", BLUE)
        
        self.play(GrowFromCenter(numeric_value))
        self.end_fragment()
        self.play(ShrinkToCenter(numeric_value))
        self.end_fragment()

        self.play(FadeOut(radius, result))
        self.end_fragment()

        general_radius = MathTex("r").set_color(YELLOW)
        general_radius.next_to(line, UP)

        self.play(Write(general_radius))
        self.end_fragment()

        general_perimeter = MathTex("P", "=", "2\\pi", "r\\relax").to_edge(DOWN)
        general_perimeter.set_color_by_tex_to_color_map({"P": BLUE, "r\\relax": YELLOW})

        self.play(Write(general_perimeter))
        self.play(Circumscribe(general_perimeter))
        self.end_fragment()

        general_perimeter2 = MathTex("P", "=\\relax", "C", "(", "r\\relax", ")", "=", "2\\pi", "r\\relax")
        general_perimeter2.to_edge(DOWN)
        general_perimeter2.set_color_by_tex_to_color_map({
            "P": BLUE, "C": GREEN, "r\\relax": YELLOW
        })

        self.play(TransformMatchingTex(general_perimeter, general_perimeter2))
        self.end_fragment()

        general_perimeter3 = MathTex("C", "(", "r\\relax", ")", "=", "2\\pi", "r\\relax").to_edge(DOWN)
        general_perimeter3.set_color_by_tex_to_color_map({
            "P": BLUE, "C": GREEN, "r\\relax": YELLOW
        })

        self.play(TransformMatchingTex(general_perimeter2, general_perimeter3))
        self.play(Circumscribe(general_perimeter3))
        self.end_fragment()

        specific_perimeter = MathTex(
            "C", "(", "2\\relax\\relax", ")", "=", "2\\pi", "(\\relax", "2\\relax", ")\\relax"
        ).to_edge(DOWN)
        specific_perimeter.set_color_by_tex_to_color_map({
            "C": GREEN,
            "2\\relax": YELLOW
        })

        self.play(
            ReplacementTransform(general_radius, radius),
            TransformMatchingTex(general_perimeter3, specific_perimeter)
        )
        self.end_fragment()

        specific_perimeter2 = MathTex("C", "(", "2\\relax\\relax", ")", "=", "4\\pi").to_edge(DOWN)
        specific_perimeter2.set_color_by_tex_to_color_map({
            "C": GREEN,
            "2\\relax": YELLOW
        })

        self.play(ReplacementTransform(specific_perimeter, specific_perimeter2))
        self.play(Circumscribe(specific_perimeter2))
        self.end_fragment()
        
        approx = MathTex("C", "(", "2\\relax\\relax", ")", "\\approx", str(np.round(4 * PI, decimals=4)))
        approx.next_to(specific_perimeter2, UP)
        approx.set_color_by_tex_to_color_map({
            "C": GREEN,
            "2\\relax": YELLOW
        })

        self.play(GrowFromCenter(approx))
        self.end_fragment()
        self.play(ShrinkToCenter(approx))
        self.end_fragment()

        self.play(FadeOut(group, specific_perimeter2, radius))
        self.end_fragment()


class Example2(PresentationScene):
    def construct(self):
        title = Text("Funciones que quizá ya conocías").to_edge(UP)
        self.add(title)
        self.end_fragment()

        rec = Rectangle(color=BLUE).set_fill(BLUE, opacity=0.7).scale(1.5)
        x_tex = MathTex("x").set_color(YELLOW)
        x_tex.next_to(rec, DOWN)
        y_tex = MathTex("y").set_color(BLUE)
        y_tex.next_to(rec, RIGHT)

        self.play(Write(rec))
        self.end_fragment()
        self.play(Write(x_tex))
        self.end_fragment()
        self.play(Write(y_tex))
        self.end_fragment()
        
        eq = MathTex("x", "+", "{2}", "y", "=", "{600}").to_edge(DOWN)
        eq.set_color_by_tex_to_color_map({"x": YELLOW, "y": BLUE})
        
        self.play(Write(eq))
        self.end_fragment()

        eq2 = MathTex("{2}", "y", "=", "{600}", "-", "x").to_edge(DOWN)
        eq2.set_color_by_tex_to_color_map({"x": YELLOW, "y": BLUE})

        self.play(TransformMatchingTex(eq, eq2))
        self.end_fragment()

        eq3 = MathTex("y", "=", "{600", "-", "x", "\\over", "2}").to_edge(DOWN)
        eq3.set_color_by_tex_to_color_map({"x": YELLOW, "y": BLUE})
        
        self.play(TransformMatchingTex(eq2, eq3))
        self.play(Circumscribe(eq3))
        self.end_fragment()

        y_tex2 = MathTex("{600", "-", "x", "\\over", "2}").next_to(rec, RIGHT)
        y_tex2.set_color_by_tex("x", YELLOW)

        self.play(FadeOut(eq3), ReplacementTransform(y_tex, y_tex2))
        self.end_fragment()

        area = MathTex(
            "A", "(", "x", ")", "=", "{x}", "\\left(", "{600", "-", "x", "\\over", "2}", "\\right)"
        ).to_edge(DOWN)
        area.set_color_by_tex_to_color_map({"A": GREEN, "x": YELLOW})

        self.play(Write(area))
        self.end_fragment()
        
        area2 = MathTex("A", "(", "x", ")", "=", "{x", "(", "{600}", "-", "x", ")", "\\over", "2}")
        area2.to_edge(DOWN)
        area2.set_color_by_tex_to_color_map({"A": GREEN, "x": YELLOW})

        self.play(TransformMatchingTex(area, area2))
        self.play(Circumscribe(area2))
        self.end_fragment()

        self.play(FadeOut(title, rec, x_tex, y_tex2, area2))
        self.end_fragment()


class TableOfContents2(TableOfContents):
    def construct(self):
        blst = self.table_of_contents[1]
        blst[0].scale(1.2).set_color(YELLOW)
        self.add(self.table_of_contents)
        self.end_fragment()
        self.play(
            blst[0].animate.scale(1/1.2).set_color(WHITE),
            blst[1].animate.scale(1.2).set_color(YELLOW)
        )
        self.end_fragment()


class QueEsFuncion(PresentationScene):
    def construct(self):
        titulo = Text("Concepto de función").to_edge(UP)
        self.add(titulo)
        self.end_fragment()

        definicion = Text(
            "Es una regla que asigna a cada valor de la variable un único valor", slant=ITALIC,
            t2c={"asigna": BLUE, "único": YELLOW}
        ).scale(0.7)
        self.play(Write(definicion))
        self.end_fragment()
        
        self.play(FadeOut(titulo, definicion))
        self.end_fragment()


class TableOfContents3(TableOfContents):
    def construct(self):
        blst = self.table_of_contents[1]
        blst[1].scale(1.2).set_color(YELLOW)
        self.add(self.table_of_contents)
        self.end_fragment()
        self.play(
            blst[1].animate.scale(1/1.2).set_color(WHITE),
            blst[2].animate.scale(1.2).set_color(YELLOW)
        )
        self.end_fragment()


class Ejercicio1(PresentationScene):
    def construct(self):
        titulo = Text("Ejercicios y problemas de aplicación").to_edge(UP)
        self.add(titulo)
        self.end_fragment()
        
        problema = Text("¿Cuál es el dominio y recorrido de la primera función vista?").scale(0.7)
        func_tex = MathTex("C", "(", "r\\relax", ")", "=", "2\\pi", "r\\relax")
        func_tex.set_color_by_tex_to_color_map({"C": GREEN, "r\\relax": YELLOW})
        ejercicio1 = VGroup(problema, func_tex).arrange(DOWN).next_to(titulo, DOWN)

        self.play(Write(ejercicio1))
        self.end_fragment()
        
        r_tracker = ValueTracker(1)
        center = Dot(color=ORANGE).to_corner(DL).shift(1.5*UR)
        circle = always_redraw(lambda: Circle(radius=r_tracker.get_value()).move_to(center))
        line = always_redraw(lambda: Line(circle.get_center(), circle.get_right()))
        r_tex = MathTex("r").set_color(YELLOW).next_to(line, UP)
        group = VGroup(line, center, r_tex, circle)

        self.play(Write(group))
        self.end_fragment()

        def func():
            mob = DecimalNumber(r_tracker.get_value(), num_decimal_places=1)
            mob.set_color(YELLOW)
            mob.scale(r_tracker.get_value())
            mob.next_to(line, UP)
            return mob

        r_tex2 = always_redraw(func)

        self.play(ReplacementTransform(r_tex, r_tex2))
        group.remove(r_tex)
        self.end_fragment()
        self.play(r_tracker.animate.set_value(0.5))
        self.end_fragment()
        self.play(r_tracker.animate.set_value(1.5))
        self.end_fragment()

        r_condition = MathTex("r", ">", "0").set_color_by_tex("r", YELLOW).to_corner(DR)
        C_domain = MathTex("\\mathrm{Dom}_", "C\\relax", "=", "\\mathbb{R}^+").to_corner(DR)
        C_domain.set_color_by_tex_to_color_map({"C\\relax": GREEN, "\\mathrm{Dom}": YELLOW})
        
        self.play(Write(r_condition))
        self.end_fragment()
        self.play(ReplacementTransform(r_condition, C_domain))
        self.play(Circumscribe(C_domain))
        self.end_fragment()

        self.play(FadeOut(C_domain))
        self.end_fragment()

        C_range = MathTex("\\mathrm{Rec}_", "C\\relax", "=", "\\mathbb{R}^+").to_corner(DR)
        C_range.set_color_by_tex_to_color_map({"C\\relax": GREEN, "\\mathrm{Rec}": BLUE})
        self.play(Write(C_range))
        self.play(Circumscribe(C_range))
        self.end_fragment()

        self.play(FadeOut(ejercicio1, group, r_tex2, C_range))
        self.end_fragment()


class Ejercicio2(PresentationScene):
    def construct(self):
        titulo = Text("Ejercicios y problemas de aplicación").to_edge(UP)
        self.add(titulo)
        self.end_fragment()

        problema = Text("¿Cuál es el dominio de la segunda función vista?").scale(0.7)
        area = MathTex("A", "(", "x", ")", "=", "{x", "(", "{600}", "-", "x", ")", "\\over", "2}")
        area.set_color_by_tex_to_color_map({"A": GREEN, "x": YELLOW})
        ejercicio2 = VGroup(problema, area).arrange(DOWN)
        
        self.play(Write(ejercicio2))
        self.end_fragment()

        ineq1 = MathTex("x\\relax", ">", "0").set_color_by_tex("x", YELLOW).to_corner(DL)
        ineq2 = MathTex("{600", "-", "x\\relax", "\\over", "2}", ">", "0").set_color_by_tex("x\\relax", YELLOW)
        ineq2.to_corner(DR)

        self.play(Write(ineq1), Write(ineq2))
        self.play(Circumscribe(ineq1))
        self.end_fragment()

        ineq2_2 = MathTex("{600}", "-", "x\\relax", ">", "0").set_color_by_tex("x\\relax", YELLOW).to_corner(DR)

        self.play(TransformMatchingTex(ineq2, ineq2_2))
        self.end_fragment()

        ineq2_3 = MathTex("{600}", ">", "x\\relax").set_color_by_tex("x\\relax", YELLOW).to_corner(DR)
        
        self.play(TransformMatchingTex(ineq2_2, ineq2_3))
        self.end_fragment()

        ineq2_4 = MathTex("x\\relax", "<", "600").set_color_by_tex("x\\relax", YELLOW).to_corner(DR)
        
        self.play(TransformMatchingTex(ineq2_3, ineq2_4))
        self.play(Circumscribe(ineq2_4))
        self.end_fragment()

        group = VGroup(ineq1, ineq2_4)
        ineq = MathTex("0", "<\\relax", "x\\relax", "<", "600").set_color_by_tex("x\\relax", YELLOW)
        ineq.to_edge(DOWN)
       
        self.play(TransformMatchingTex(group, ineq))
        self.play(Circumscribe(ineq))
        self.end_fragment()

        domain = MathTex("\\mathrm{Dom}_", "A", "=", "]0,600[").to_edge(DOWN)
        domain.set_color_by_tex_to_color_map({"\\mathrm{Dom}_": YELLOW, "A": GREEN})

        self.play(ReplacementTransform(ineq, domain))
        self.play(Circumscribe(domain))
        self.end_fragment()

        self.play(FadeOut(titulo, ejercicio2, domain))
        self.end_fragment()


class Outro(PresentationScene):
    def construct(self):
        thank_you = Text("¡Muchas gracias por ver!")
        youtube = brand.youtube_square.set_color(RED)
        group = VGroup(thank_you, youtube).arrange(DOWN)

        self.play(Write(group))
        self.play(ApplyWave(thank_you))
        self.play(Indicate(youtube))
        self.end_fragment()


# export(guarantee_existence(".\\plugin\\manim"))