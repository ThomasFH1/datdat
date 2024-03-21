
def les_salfil(salfil):
    områder = {}
    with open(f"files_needed/{salfil}", "r") as f:
        dato = f.readline().strip()

        for line in f:
            if not line[0].isdigit():
                last_område = line.strip()
                områder[last_område] = []
            else:
                ny_rad = [int(seat)
                            for seat in line.strip().replace("x", "")]
                områder[last_område].append(ny_rad)
    return områder, dato