import scanner.antivirus as antivirus


def scan_file(file_name, file_stream):
    antivirus_passed = antivirus.scan_virus(file_stream)

    return antivirus_passed
