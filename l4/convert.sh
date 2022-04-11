xxd -b pantadeusz.encrypted | cut -d" " -f 2-7 | tr -d "\n" | tr -d " " > pantadeusz.encrypted.binary
