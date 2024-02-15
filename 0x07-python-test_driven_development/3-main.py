#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Ibiso", "pretty")
say_my_name("Ibiso Harrison the", "coder")
say_my_name("Ogariawo", "C")

try:
    say_my_name(12, "Caramel")
except Exception as e:
    print(e)
