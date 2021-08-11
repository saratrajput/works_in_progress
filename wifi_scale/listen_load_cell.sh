#!/bin/bash

nc -k -l 3000 | while IFS= read -r line; do printf '%s %s\n' "$(date)" "$line"; done >> new_out.txt
