# -*- coding: utf-8 -*-

"""Tests for autocrop"""

import os
import shutil
import sys

try:
    import mock
except ImportError:
    from unittest import mock
import pytest
import cv2

from autocrop.autocrop import (
        cli,
        crop_folder,
)

PY3 = (sys.version_info[0] >= 3)


@pytest.fixture()
def integration():
    # Setup
    path_i = 'tests/test'
    path_o = 'tests/crop'
    shutil.copytree('tests/data', path_i)
    yield

    # Teardown
    shutil.rmtree(path_i)
    try:
        shutil.rmtree(path_o)
    except OSError:
        pass


def test_crop_folder_overwrites_when_same_input_and_output(integration):
    sys.argv = ['', '--no-confirm', '-i', 'tests/test', '-o', 'tests/test']
    cli()
    output_files = os.listdir(sys.argv[-1])
    assert len(output_files) == 10


@mock.patch('autocrop.autocrop.crop')
def test_crop_folder_overwrites_when_no_output(mock_crop, integration):
    mock_crop.return_value = None
    assert mock_crop.call_count == 0
    crop_folder('tests/test', None)
    assert mock_crop.call_count == 9


@mock.patch('autocrop.autocrop.crop', lambda *args: None)
def test_images_files_copied_over_if_output_dir_specified(integration):
    sys.argv = ['', '-i', 'tests/test', '-o', 'tests/crop']
    cli()
    output_files = os.listdir(sys.argv[-1])
    assert len(output_files) == 9


@mock.patch('autocrop.autocrop.confirmation', lambda *args: True)
def test_image_files_overwritten_if_no_output_dir(integration):
    sys.argv = ['', '-i', 'tests/test']
    cli()
    # We have the same number of files
    output_files = os.listdir(sys.argv[-1])
    assert len(output_files) == 10
    # Images with a face have been cropped
    shape = cv2.imread('tests/test/king.jpg').shape
    assert shape == (500, 500, 3)


@mock.patch('autocrop.autocrop.confirmation', lambda *args: True)
@mock.patch('autocrop.autocrop.crop_file')
def test_calling_autocrop_with_filename_crops_it(mock_crop_file, integration):
    mock_crop_file.return_value = None
    sys.argv = ['', 'tests/test/king.jpg']
    assert mock_crop_file.call_count == 0
    cli()
    # We've made a call to crop_file
    assert mock_crop_file.call_count == 1


@mock.patch('autocrop.autocrop.confirmation', lambda *args: True)
@mock.patch('autocrop.autocrop.crop_file')
def test_cli_input_and_filename_raises_error(mock_crop_file, integration):
    mock_crop_file.return_value = None
    sys.argv = ['', 'tests/test/king.jpg', '-i', 'tests/data']
    with pytest.raises(SystemExit) as e:
        cli()
    assert e.type == SystemExit
    print(e.__name__)
    assert 'both' in str(e)
