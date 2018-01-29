# Dev notes for issue 25
- Add `-o`, `--output` flag to specify directory where cropped images are to be dumped.
    * Error out if output folder set to current directory, i.e. `-o .`
    * If directory doesn't exist yet, create it.
    * If no face can be found in an image in batch, it is still copied over to `-o` folder.
    * If no output folder is added, ask for confirmation (`[Y]/n`), and destructively crop images in-place.
        + Confirmation can be skipped with `--no-confirm` flag.
- Use `-i`, `--input` flags as synonyms for `-p` or `--path`: symmetrical in meaning to "output".
    * To become standard nomenclature in documentation.
- `--input` or `--path` flag to become optional.
    * Standard behaviour without input folder will be to non-recursively process all images in immediate folder, i.e. `-p .` as currently implemented.
