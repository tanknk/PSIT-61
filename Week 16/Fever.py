"""Fever"""
def main(temp):
    """Print Fever"""
    print('No Fever' if 36 <= temp < 38 else 'Mild Fever' if 38 <= temp < 39 else \
        'High Fever' if 39 <= temp < 40 else 'Very High Fever')
main(float(input()))
