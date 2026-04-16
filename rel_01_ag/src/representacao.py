def bin_to_real(binary, min_val, max_val):
    decimal = int(binary, 2)
    max_decimal = 2**len(binary) - 1
    return min_val + (decimal / max_decimal) * (max_val - min_val)


def decode_individuo(individuo):
    x_bin = individuo[:16]
    y_bin = individuo[16:]

    x = bin_to_real(x_bin, -5, 5)
    y = bin_to_real(y_bin, -5, 5)

    return x, y