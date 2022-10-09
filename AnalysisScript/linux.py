import sh

def linuxTools(file_name):
    dump_file = open(r"results.txt", 'a')

    file = ["file:", sh.file(file_name)]
    dump_file.writelines[file]

    # might add OALabs/hashdb
    # https://github.com/OALabs/hashdb
    shasums = ["shasums:", sh.sha256sum(file_name) + "sha256",
               sh.sha512sum(file_name) + "sha512"]
    dump_file.writelines[shasums]

    #possibly add grep and find for string parseing
    string = ["strings:", sh.strings(file_name)]
    dump_file.writelines[string]

    ldd_command = ["ldd:", sh.ldd(file_name)]
    dump_file.writelines[ldd_command]
    
    nm_command = ["nm:", sh.nm(file_name)]
    dump_file.writelines[nm_command]

    objdump_command = ["objdump:", sh.objdump("-M intel -d " + file_name)]
    dump_file.writelines[objdump_command]

    read_elf = ["readelf:", sh.readelf("-a " + file_name)]
    dump_file.writelines[read_elf]
    
    # find packers 
    upx = ["upx:", sh.grep("upx" + sh.strings(file_name))]
    dump_file.writelines[upx]

    dump_file.close()
