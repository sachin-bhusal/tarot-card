import pytest
import project

def main():
    #test_button_click()
    test_GUI()
    test_tips_title()
    test_tips_text()

def test_tips_text():
    assert project.tips_text()=="Choose exactly 4 cards and close the window when done.\nRelax and mindfully chose your cards, else you might not get an accurate reading."

def test_GUI():
    with pytest.raises(TypeError):
        project.GUI(1)
        project.GUI("spring")


def test_tips_title():
    assert project.tips_title() == "Tips for choosing cards:"

if __name__ == "__main__":
    main()