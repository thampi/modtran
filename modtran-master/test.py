from getpass import getpass
import matplotlib.pyplot as plt

#mpl.use('Qt5Agg')  # or can use 'TkAgg', whatever you have/prefer
import modtran

# Sample tape5 params
# Doesn't work for some reason. Mostly issue with tape5 formatting
# output = modtran.run(username='gt6863',    # input('Enter CIS username: '),
#                      password='EldenRingCantWait',    # getpass(prompt='Enter CIS password: '),
#                      # default hostname : grissom.cis.rit.edu
#                      hostname='aldrin.cis.rit.edu',
#                      # CARD 1
#                      # MODTRN='M',
#                      # MODEL=2,
#                      ITYPE=3,
#                      IMULT=0,
#                      IM=1,
#                      TPTEMP=291.750,
#                      SURREF=0.200,
#                      # CARD 1A
#                      DIS='F',
#                      # DISAZM='T',
#                      # NSTR=8,
#                      LSUN='F',
#                      ISUN=0,
#                      CO2MX=0.0,
#                      H2OSTR='330.0000',
#                      # CARD 2
#                      # IHAZE=1,
#                      # ISEASN=0,
#                      # IVULCN=0,
#                      ICSTL=1,
#                      IVSA=1,
#                      # VIS=0.00000,
#                      # WSS=0.00000,
#                      # RAINRT=0.00000,
#                      # GNDALT=0.00000,
#                      # CARD 3
#                      H1=700.000,
#                      # H2=0.000,
#                      # ANGLE=180.000,
#                      LENN=0,
#                      # CARD 3A1
#                      IPARM=2,
#                      # IPH=2,
#                      IDAY=40,
#                      # ISOURCE=0,
#                      # CARD 3A2
#                      # PARM1=0.000,
#                      PARM2=30.000,
#                      # ANGLEM=0.000,
#                      G=0.000,
#                      # CARD 4
#                      V1=0.4000,
#                      # V2=1.0000,
#                      DV=0.0010
#                      # FLAGS='mraa',    # CAPS in code
#                      # CARD 4A
#                      # NSURF=2,
#                      # AATEMP=0,
#                      # # CARD 5
#                      # IRPT=0
#                      )

output = modtran.run(input('Enter CIS username: '),
                     getpass(prompt='Enter CIS password: '),
                     # default hostname : grissom.cis.rit.edu
                     hostname='aldrin.cis.rit.edu',
                     H2OSTR='g0.001',
                     VIS=-0.052,
                     SURREF=0.002,
                     PARM2=5.0,
                     IPARM=12,
                     IMULT=-1,
                     IHAZE=1,
                     DIS='T',
                     DISAZM='T',
                     NSTR=8,
                     ANGLE=180.0,
                     H1=700.0,
                     H2=0.0,
                     V1=0.4,
                     V2=2.5,
                     DV=0.001)

# output is a dictionary that includes the tape5 and tape7.scn files, as well
# as the data columns from tape7.scn

print('INPUT TAPE5 FILE :\n', output['tape5'])
print('OUTPUT FROM /dirs/pkg/Mod4v3r1 on CIS linux machine :\n', output['tape7.scn'])
# print('OUTPUT PARSED INTO PYTHON :\n', output.items())
# plt.figure(0)
# plt.plot(output['WAVELEN MCRN'], output['TOTAL RAD'], 'k', label='TOTAL RAD')
# plt.plot(output['WAVELEN MCRN'], output['GRND RFLT'], 'b', label='GRND RFLT')
# plt.xlabel(r'Wavelength [$\mu$m]')
# plt.ylabel(r'Radiance [W/cm$^2 \cdot$sr$\cdot \mu$m]')
# plt.legend()
# plt.show()
