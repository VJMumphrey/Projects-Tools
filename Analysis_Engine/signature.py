"""
Unicorn to emulate code
Keystone to Assemble code
Capstone to Disassemble
"""

from unicorn import Uc, UC_ARCH_X86, UC_MODE_64, UcError
from unicorn.x86_const import UC_X86_REG_RDI, UC_X86_REG_RAX
from keystone import Ks, KS_ARCH_X86, KS_MODE_64, KsError
from capstone import Cs, CS_ARCH_X86, CS_MODE_64, CsError

# generate signature for functions in code
def gensignature() -> None:
    pass

"""
store the functions into a defined database
database is used to compare code genetics
reduce RE time
"""
def store() -> None:
    pass
