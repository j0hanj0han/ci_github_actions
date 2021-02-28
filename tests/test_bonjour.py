from ci_github_actions import bonjour


def test_helloworld():
    # given

    # when
    result = bonjour.helloworld()
    # then
    assert result == "Launched by github actions"