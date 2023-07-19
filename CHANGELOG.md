# CHANGELOG



## v3.0.0 (2023-07-19)

### Breaking

* feat(vue23): Support vue2 and vue3 with latest plotly lib

BREAKING CHANGE: By updating to the latest plotly and supporting vue2/3 we may have introduced some breaking behavior ([`63dc776`](https://github.com/Kitware/trame-plotly/commit/63dc776278ff71785d0403faea5f54c02e5f4396))

### Unknown

* Merge pull request #3 from Kitware/vue3

feat(vue23): Support vue2 and vue3 with latest plotly lib ([`86a0e84`](https://github.com/Kitware/trame-plotly/commit/86a0e84c1d3627e5c5a3224cdc150d16b1c8628c))


## v2.1.1 (2023-02-23)

### Fix

* fix(version): add __version__

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`58100dd`](https://github.com/Kitware/trame-plotly/commit/58100dd11a4c601e5b1efe7105f0489b7b5d865e))


## v2.1.0 (2022-11-18)

### Chore

* chore(semantic-release): bump version to latest

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`487343d`](https://github.com/Kitware/trame-plotly/commit/487343dadd8c38d759634c32cd33831e3235f625))

### Documentation

* docs(coverage): remove codecov PR comment

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`5196cc3`](https://github.com/Kitware/trame-plotly/commit/5196cc37347942375e5bc2a372bd7fc13ed9c6ad))

* docs(coverage): add .coveragerc

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`dc825d0`](https://github.com/Kitware/trame-plotly/commit/dc825d05f815583030be00dfeaf1dce007cb463c))

* docs(ci): add coverage and codecov upload

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`3862800`](https://github.com/Kitware/trame-plotly/commit/38628009ead520307f6b29144da11a5b92ad10ae))

* docs(readme): add CI badge

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`32ff20a`](https://github.com/Kitware/trame-plotly/commit/32ff20a03d2c1508c4984554cb913610a16ff26a))

* docs(contributing): add CONTRIBUTING.rst

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`22b5908`](https://github.com/Kitware/trame-plotly/commit/22b5908eddad7607c8b01fe43a076952993281b0))

### Feature

* feat(figure): add ability to set state variable name

This is done so that the same underlying state variable can be used for two separate figures.

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`e09a072`](https://github.com/Kitware/trame-plotly/commit/e09a072347e3b03234d90028a826634cd334a1bf))

### Unknown

* Merge pull request #1 from Kitware/state-variable-name

feat(figure): add ability to set state variable name ([`407c5b0`](https://github.com/Kitware/trame-plotly/commit/407c5b0314adac4862866bbba260e000c05edaf9))


## v2.0.1 (2022-05-27)

### Documentation

* docs(api): add missing information ([`a4521a7`](https://github.com/Kitware/trame-plotly/commit/a4521a76c49978b86db205bf6416b5504a05a517))

### Fix

* fix: add initial CI, including semantic release

This also fixes any pre-commit issues

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`cf33a87`](https://github.com/Kitware/trame-plotly/commit/cf33a87eb02f0968dc224ffd74f511402fa5a667))

* fix(rc5): trame.widgets initialize ([`e9801ff`](https://github.com/Kitware/trame-plotly/commit/e9801ffb4a6b1a36a6b1e0f3fe0b63a561bb107a))

### Unknown

* Add __all__ to plotly widgets

Signed-off-by: Patrick Avery &lt;patrick.avery@kitware.com&gt; ([`6b174a6`](https://github.com/Kitware/trame-plotly/commit/6b174a6a0925391344e05cfb6e451c3d21086000))

* Trame v2 - Plotly widgets

This initial commit gather the first stage of what the Plotly trame widgets represent for trame 2.0.0. ([`57dd546`](https://github.com/Kitware/trame-plotly/commit/57dd5463d52b1cfd6085f9c2c4def6ba18221dc0))
