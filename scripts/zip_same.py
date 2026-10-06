#!/usr/bin/env python3
"""
zip_same.py A B — exit 0 if two zip archives hold the same content.

Same content means: the same set of entry names, and for each entry the same
uncompressed bytes (compared recursively for a member that is itself a zip)
and the same executable bit. Entry order, timestamps,
compression level, permission bits other than +x, and extra fields are
ignored.

check.sh uses this when a rebuilt archive (.skill, .docx, .xlsx, .zip) is
byte-different from the committed one: if the content is the same, the
difference is the build platform (Info-ZIP walks directories in filesystem
order, which differs between APFS and ext4; zlib builds can differ), not a
stale source, so it is not reported. Stdlib only.
"""

import io
import sys
import zipfile


def summary(source):
    """{name: (executable, content)}; a member that is itself a zip (a .docx
    or .xlsx inside the template bundle) is compared by its own content too,
    since its bytes carry the same platform noise."""
    with zipfile.ZipFile(source) as z:
        out = {}
        for info in z.infolist():
            mode = (info.external_attr >> 16) & 0o111
            data = z.read(info.filename)
            if data[:4] == b"PK\x03\x04":
                try:
                    data = summary(io.BytesIO(data))
                except zipfile.BadZipFile:
                    pass
            out[info.filename] = (bool(mode), data)
        return out


def main():
    if len(sys.argv) != 3:
        print("usage: zip_same.py A B", file=sys.stderr)
        return 2
    try:
        return 0 if summary(sys.argv[1]) == summary(sys.argv[2]) else 1
    except (OSError, zipfile.BadZipFile):
        return 1


if __name__ == "__main__":
    sys.exit(main())
