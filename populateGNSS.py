def populateGNSS():
    gnss_led.on()
    uart_gnss.read()
    fix = False
    while not fix:
        if uart_gnss.any():
            uart_in = uart_gnss.read().decode()
            for x in uart_in:
                gps_data.update(x)
            fix = gps_data.valid
        else:
            utime.sleep_ms(350)
    gnss_led.off()