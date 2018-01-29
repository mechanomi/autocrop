# Dev notes for autocrop issue 30
* [ ] `autocrop filename.jpg` should crop the image in place and ask for confirmation.
    - [ ] Flag `--force` or `-f` to bypass prompt.
* [ ] `autocrop filename.jpg -o folder` places the cropped image in folder.
    - [ ] If that directory doesn't exist, create it.
    - [ ] If `folder/filename.jpg` already exists, prompt, bypass with `-f`
* [ ] `autocrop filename.jpg -i folder` doesn't make sense to me. Error out.
* [ ] `autocrop -w` and `-H`: same behaviour as currently implemented.
* [ ] Standarsize error codes for single files.
    - [ ] 0 for success
    - [ ] 1 for failure
