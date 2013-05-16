"""Collection of commonly used physical units.

"""

import math

import scipy.constants

from basic import unit, converter

# Multiples
deca  = converter("dc","deca", scipy.constants.deka)
hecto = converter("h", "hecto",scipy.constants.hecto)
kilo  = converter("k", "kilo", scipy.constants.kilo)
mega  = converter("M", "mega", scipy.constants.mega)
giga  = converter("G", "giga", scipy.constants.giga)
tera  = converter("T", "tera", scipy.constants.tera)
peta  = converter("P", "peta", scipy.constants.peta)
exa   = converter("E", "exa",  scipy.constants.exa)
zetta = converter("Z", "zetta",scipy.constants.zetta)
yotta = converter("Y", "yotta",scipy.constants.yotta)
multiples = [deca, hecto, kilo, mega, giga, tera, peta, exa, zetta, yotta]

# Fractions
deci  = converter("d", "deci", scipy.constants.deci)
centi = converter("c", "centi",scipy.constants.centi)
milli = converter("m", "milli",scipy.constants.milli)
micro = converter("mu","micro",scipy.constants.micro)
nano  = converter("n", "nano", scipy.constants.nano)
pico  = converter("p", "pico", scipy.constants.pico)
femto = converter("f", "femto",scipy.constants.femto)
atto  = converter("a", "atto", scipy.constants.atto)
zepto = converter("z", "zepto",scipy.constants.zepto)
yocto = converter("y", "yocto",scipy.constants.yocto)
fractions = [deci, centi, milli, micro, nano, pico, femto, atto, zepto, yocto]

def loadconverters(theunit):
    """This function derives and stores in the module multiples of
       ten from an original unit.

    Parameters
    ----------
    theunit : unit

    Example
    -------
    >>> import units
    >>> units.loadconverters(units.V) # derives all muliples of voltage
    >>> 2.5 * units.mV
    """ 
    if not isinstance(theunit, unit): return 
    for converter in multiples+fractions:
        msymb = converter.symbol + theunit.symbol
        mname = converter.name + theunit.name
        globals()[mname] = globals()[msymb] = converter * theunit
    return

# Arbitrary or dimensionless units
au = unit(symbol='a.u.',name='arbitrary unit') 
radian    = rad = unit(symbol='rad',name='radian')
steradian = sr  = unit(symbol='sr',name='steradian')
degree    = deg = unit(symbol='deg',name='degree',
                       converter=converter(ratio=math.pi/180.))

# International System of Units, SI base units
for usymb,uname in [['m','metre'],['kg','kilogram'],['s','second'],
                    ['A','ampere'],['K','kelvin'],['mol','mole'],
                    ['cd','candela']]:
    globals()[usymb] = unit(symbol=usymb,name=uname)
    globals()[usymb].dim = [[globals()[usymb],1]]
    globals()[uname] = globals()[usymb]
loadconverters(metre)

# SI Derived units
hertz = Hz = unit(symbol='Hz',name='hertz',unit=s**-1)         # Frequency
becquerel = Bq = unit(symbol='Bq',name='becquerel',unit=s**-1) # Radioactivity
newton = N = unit(symbol='N',name='newton',unit=kg*m*(s**-2))  # Force 
pascal = Pa = unit(symbol='Pa',name='pascal',unit=N*(m**-2))   # Pressure
joule = J = unit(symbol='J',name='joule',unit=N*m)         # Energy 
watt = W = unit(symbol='W',name='watt',unit=J/s)           # Power 
gray = Gy = unit(symbol='Gy',name='gray',unit=J/kg)        # Absorbed dose
sievert = Sv = unit(symbol='Sv',name='sievert',unit=J/kg)  # Equivalent dose
coulomb = C = unit(symbol='C',name='coulomb',unit=s*A)  # Electric charge
volt = V = unit(symbol='V',name='volt',unit=J/C)        # Voltage
farad = F = unit(symbol='F',name='farad',unit=C/V)      # Electric capacitance
ohm = unit(name='ohm',unit=V/A)                         # Electric resistance
siemens = unit(symbol='S',name='siemens',unit=C**-1)    # Electric conductance
weber = Wb = unit(symbol='Wb',name='weber',unit=J/A)       # Magnetic flux
tesla = T = unit(symbol='T',name='tesla',unit=Wb*(m**-2))  # Magnetic field
henry = H = unit(symbol='H',name='henry',unit=Wb/A)        # Inductance 
lumen = lm = unit(symbol='lm',name='lumen',unit=cd*sr)     # Luminous flux 
lux = lx = unit(symbol='lx',name='lux',unit=lm*(m**-2))    # Illuminance
katal = kat = unit(symbol='kat',name='katal',unit=mol/s)   # Catalytic activity

# Widely used non SI units
# time
htomin = mintos = converter("","",60)
daytoh = converter("","",24)
weektoday = converter("","",7)
minute = min = unit(symbol='min',name='minute',unit=mintos*s)
hour = h = unit(symbol='h',name='hour',unit=htomin*min)
day = d = unit(symbol='d',name='day',unit=daytoh*h)
week = unit(name='week',unit=weektoday*day)
# length
angstrom = unit(name='angstrom',unit=daytoh*h)
