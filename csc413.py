import sys, os

try:
    input = int(sys.argv[1])
except:
    print("Invalid input")

if input == 0:
    os.startfile("Strelitzia_OBJ\\strelitzia_1.obj")
elif input == 1:
    os.startfile("Orchid_Phalaenopsis_OBJ\\orchid.obj")
elif input == 2:
    os.startfile("Hoewa_Forsteriana_OBJ\\hoewa_Forsteriana_1.obj")
elif input == 3:
    os.startfile("Matteuccia_Struthiopteris_OBJ\\matteucia_struthiopteris_1.obj")
elif input == 4:
    os.startfile("Anemone_Hybrida_OBJ\\anemone_hybrida.obj")
elif input == 5:
    os.startfile("Hydrangea_sp_Hortensia_OBJ\\FL48_1.obj")
else:
    print("No Valid File")
