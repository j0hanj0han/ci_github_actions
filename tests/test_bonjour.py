from cigithubactions import bonjour


def test_helloworld():
    # given

    # when
    result = bonjour.helloworld()
    # then
    assert result == "Launched by github actions"