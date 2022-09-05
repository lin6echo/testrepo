import mymodule2
mymodule2.func_in_module()

import mymodule2 as mm
mm.func_in_module()

from mymodule2 import func_in_module
func_in_module()

from mymodule2 import *
func_in_module()