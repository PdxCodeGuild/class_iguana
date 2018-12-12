def rot13(s, rot):
    result = ""
    rot = int(rot)
    # Loop over characters.
    for v in s:
        # Convert to number with ord.
        c = ord(v)
        print(v)
        print(c)
        print

        # Shift number back or forward depending if character is capitalized or not.
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= rot
            else:
                c += rot
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= rot
            else:
                c += rot

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result

print(rot13("Ra|SrA|", 17))
