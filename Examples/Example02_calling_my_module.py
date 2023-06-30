import sys
import Example02_my_module

if len(sys.argv) == 2:
    Example02_my_module.hello(sys.argv[1])
 # Because I used "__name__" in my_module, main() is running only if I specifically calling it
    Example02_my_module.main()