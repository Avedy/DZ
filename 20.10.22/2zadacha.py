"""
Напишите программу добавляющую в рецепт бутерброда ингридиенты "Салат" и "Ананасы" с помощью декораторов.
"""


def buterbrod(func):
    print("Бутерброд:")
    def ingr():
        func()
    return ingr


@buterbrod
def salat():
    print("Салат")
    print("Ананас")


salat()