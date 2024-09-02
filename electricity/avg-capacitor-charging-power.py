
def calculate_average_power(capacitance, voltage, time):
    """
    Laskee kondensaattorin keskimääräisen lataustehon.

    Args:
    capacitance (float): Kondensaattorin kapasitanssi faradeina (F).
    voltage (float): Kondensaattorin jännite voltteina (V).
    time (float): Latausaika sekunteina (s).

    Returns:
    float: Keskiarvo teho milliwatteina (mW).
    """
    # Laske energia
    energy = 0.5 * capacitance * voltage ** 2
    
    # Laske keskimääräinen teho watteina
    average_power_watts = energy / time
    
    # Muunna teho milliwateiksi
    average_power_milliwatts = average_power_watts * 1000
    
    return average_power_milliwatts

# Esimerkkiarvot
capacitance = 0.047  # faradeina
voltage = 4          # volttina
time = 60           # sekunteina

# Laske keskimääräinen teho
avg_power_mW = calculate_average_power(capacitance, voltage, time)

print(f"Keskimääräinen latausteho: {avg_power_mW:.4f} mW")
