from sound import echo
from sound import bgm
from stage import sub
from stage import main
from image import character
from image import object_type


if __name__ == "__main__":
    print("Hello Game")
    print(echo.echo_play())
    print(sub.sub_play())
    print(main.main_play())
    print(character.character_play())
    print(object_type.object_type_play())
    print(bgm.bgm_play())

