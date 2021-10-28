# changelog-generator Changelog

## [0.3.1](https://github.com/Lfd4/changelog-generator/compare/0.3.0...0.3.1) (2021-10-28)

### chore

* **deps:** bump urllib3 from 1.25.7 to 1.26.5 ([37d3264](https://github.com/Lfd4/changelog-generator/commit/37d32640113693df6ee6f39af1bd31d79cf4a618))

### docs

* reformat README.md ([97b9dba](https://github.com/Lfd4/changelog-generator/commit/97b9dba4fe809d2d84d42ea0426f39e1eeb2a960))

### fix

* **tags:** sort tags before generating the changelog ([af47609](https://github.com/Lfd4/changelog-generator/commit/af476092541e6e02f8ad1f94f93028a215f7fc25))

## [0.3.0](https://github.com/Lfd4/changelog-generator/compare/v0.2.0...0.3.0) (2021-10-28)

### docs

* **update:** changelog ([3e93cff](https://github.com/Lfd4/changelog-generator/commit/3e93cff117151fd202aed53c17463456b62dc5af))

### chore

* **deps:** bump urllib3 from 1.25.7 to 1.26.5 ([6b12a67](https://github.com/Lfd4/changelog-generator/commit/6b12a6787e14af860e998b5cddd73784b22e4efb))
* migrate to pipenv ([859bb69](https://github.com/Lfd4/changelog-generator/commit/859bb6951cdb22cdf0b015db3bb3441f74092de0))

### feat

* **command:** add option to customize branch ([60b8eb7](https://github.com/Lfd4/changelog-generator/commit/60b8eb79fe8b659d7011a711273e3a18e8b9f3cc))

### refactor

* refactor ([af43b82](https://github.com/Lfd4/changelog-generator/commit/af43b827a2f67a9dd7c08729da263df63a975cd7))

## [v0.2.0](https://github.com/Lfd4/changelog-generator/compare/v0.1.7...v0.2.0) (2020-3-13)

### docs

* **update:** changelog ([4e454f5](https://github.com/Lfd4/changelog-generator/commit/4e454f5f84cdbbd2fab297488ff9ef561e539e73))
* finalize README ([f8a7a3b](https://github.com/Lfd4/changelog-generator/commit/f8a7a3b2c96721b80d224c96cf228811855b2ae6))
* add instalation section ([28718f4](https://github.com/Lfd4/changelog-generator/commit/28718f463ec5e75f57d5c8d7db9f961fb32e2549))

### feat

* commits are linked ([6010126](https://github.com/Lfd4/changelog-generator/commit/601012698a337150507b042f8d726288bf01291b))
* relices have compare links between them ([769ba2b](https://github.com/Lfd4/changelog-generator/commit/769ba2ba25abf3f7b611847a6555b110fe87cf54))

### fix

* url to commit ([d943c05](https://github.com/Lfd4/changelog-generator/commit/d943c050155654f8dc481e9dbe3ebdce6e1a8ba3))

## [v0.1.7](https://github.com/Lfd4/changelog-generator/compare/v0.1.6...v0.1.7) (2020-3-9)

### docs

* **update:** changelog ([4f93632](https://github.com/Lfd4/changelog-generator/commit/4f93632aef849536eaac5b72b48b37351e6d52a7))

### fix

* error message when CHANGELOG.md was not found ([e87ce38](https://github.com/Lfd4/changelog-generator/commit/e87ce38573bded0e6e15954a0ad3c58de2601a19))
* path joining ([c8b74da](https://github.com/Lfd4/changelog-generator/commit/c8b74da3bbb21f0c1b0edc5b83a2441ccf647664))

### refactor

* make 'types' and 'bodytags' to global variables ([789c5ee](https://github.com/Lfd4/changelog-generator/commit/789c5ee3148acb86759d75f46674c75e61a99884))
* reworked get_commits function ([03a8b10](https://github.com/Lfd4/changelog-generator/commit/03a8b105ee128b6a957ef70aacd93af21ee21505))

### feat

* add default 'types' chore, test ([aa2bec5](https://github.com/Lfd4/changelog-generator/commit/aa2bec5ecdba1aa0ff86c51e9f421a2f32d2ab7f))

## [v0.1.6](https://github.com/Lfd4/changelog-generator/compare/v0.1.5...v0.1.6) (2020-3-9)

## [v0.1.5](https://github.com/Lfd4/changelog-generator/compare/v0.1.4...v0.1.5) (2020-3-9)

### docs

* added coments to the code ([ef174b8](https://github.com/Lfd4/changelog-generator/commit/ef174b8b776a15f54eacf25d68347fc696ef0717))
* updated changelog via "add" command ([d8f3ac6](https://github.com/Lfd4/changelog-generator/commit/d8f3ac685863ac97a62bd76387eba81c3213be7d))
* add licence ([1fccc3e](https://github.com/Lfd4/changelog-generator/commit/1fccc3e1ad0861ee14ce47fe810d780a9e7bc6ba))

### refactor

* added header.py; moved header and footer from generate.py ([15d0486](https://github.com/Lfd4/changelog-generator/commit/15d0486a8c7f116f7e8a36ba51e5af990dd4d462))
* **rename:** main file ([51b7124](https://github.com/Lfd4/changelog-generator/commit/51b7124e579b9d53bb7f2fa17ace388d6edeec21))

### fix

* removed __init__.py ([3b95203](https://github.com/Lfd4/changelog-generator/commit/3b95203cdaabba9a836500821c9627fc0ea76058))
* **docs:** language ([abcc708](https://github.com/Lfd4/changelog-generator/commit/abcc708337590add73b734a7bfc6960a1905e18b))

### feat

* the add command leaves title unchanged ([e194e1e](https://github.com/Lfd4/changelog-generator/commit/e194e1ea95e3818da4ae2b383a2ec75e463cb385))

## [v0.1.4](https://github.com/Lfd4/changelog-generator/compare/v0.1.3...v0.1.4) (2020-1-3)

### chore

* **setup:** fix setup.py and make changelog an actual module ([96265d1](https://github.com/Lfd4/changelog-generator/commit/96265d1f9cc14b04db9a0af3a7e09ef3f194af31))

### fix

* updated requirements ([1c20c3d](https://github.com/Lfd4/changelog-generator/commit/1c20c3d6f5daecbfaaeece77764fcaff1efd998f))

### refactor

* moved contents of utils.py ([2eb4015](https://github.com/Lfd4/changelog-generator/commit/2eb401560c8d1de74f1ca5fec61d0ffd6c4c6dae))

## [v0.1.3](https://github.com/Lfd4/changelog-generator/compare/v0.1.2...v0.1.3) (2019-11-7)

### refactor

* better readable code (still not clean) ([1cabd73](https://github.com/Lfd4/changelog-generator/commit/1cabd73f537e1e86a33cd49e3aff5fee8b81b30d))
* error handling and more edgecase support ([f860b10](https://github.com/Lfd4/changelog-generator/commit/f860b106bdd4de10548e36e6af2ecd370a8a0cc4))
* new way of creaing commit object ([437c7ef](https://github.com/Lfd4/changelog-generator/commit/437c7efc3785871c5099c4f0b84e3456b5b99015))

### feat

* use 'printout' to only print changelog. This won't touch the changelog file ([21d72d4](https://github.com/Lfd4/changelog-generator/commit/21d72d46f16ca8e03451f8c2a321c6fac21b38aa))

### docs

* new changelog ([81a7ea0](https://github.com/Lfd4/changelog-generator/commit/81a7ea093a69d3ed61c6340ecabf7c43b657850c))

## [v0.1.2](https://github.com/Lfd4/changelog-generator/compare/v0.1.1...v0.1.2) (2019-11-6)

### fix

* multiline messages ([c6ec67f](https://github.com/Lfd4/changelog-generator/commit/c6ec67f4ddebbe358a1455f4f2540901f52f2c07))
* **multiline message:** now shown propaly i one line ([f98b530](https://github.com/Lfd4/changelog-generator/commit/f98b53054117d6e819e0717b18e9b90790be6264))

### docs

* new changelog ([b8db051](https://github.com/Lfd4/changelog-generator/commit/b8db051ac908678dc1fb908e13766463b28798ef))

## [v0.1.1](https://github.com/Lfd4/changelog-generator/compare/v0.1.0...v0.1.1) (2019-11-6)

### fix

* **date:** dates are now in yyy-mm-dd format ([b0fd272](https://github.com/Lfd4/changelog-generator/commit/b0fd272b2ee87c9081971a7d0c9ae7eb8ae02f28))

### feat

* **commands:** support to define types and bodytags ([2c09955](https://github.com/Lfd4/changelog-generator/commit/2c09955bd34c72ef42b87b59022ef89d6575b09c))

### test

* this schouldn't appear in the changelog ([1bcf9a0](https://github.com/Lfd4/changelog-generator/commit/1bcf9a04a15644f3ce8493ef9fa320637b61f795))

## [v0.1.0](https://github.com/Lfd4/changelog-generator/compare/v0.0.2...v0.1.0) (2019-11-6)

### feat

* add command ([1b766a2](https://github.com/Lfd4/changelog-generator/commit/1b766a23f5c4934d70c69cc032fbd8fb7804a1ed))

### docs

* updated readme ([e4698fe](https://github.com/Lfd4/changelog-generator/commit/e4698fe913a1124cabfa11db9cac59926bbcb20c))

## [v0.0.2](https://github.com/Lfd4/changelog-generator/compare/v0.0.1...v0.0.2) (2019-11-4)

### docs

* readme ([775192d](https://github.com/Lfd4/changelog-generator/commit/775192dc02f2bd3843488a382552cef2df73c5fc))

## v0.0.1 (2019-11-4)

### feat

* list commits test ([f96b83f](https://github.com/Lfd4/changelog-generator/commit/f96b83f91e96f1b3769eb2ea0d7663bdc0c2be5c))

### fix

* **test:** test ([f39908f](https://github.com/Lfd4/changelog-generator/commit/f39908f069326a1ddd80ebfea0b1b07fc120b3c6))

### refactor

* new structure ([cdcdc16](https://github.com/Lfd4/changelog-generator/commit/cdcdc169f926fd8a2490ba2c8f0380453bda8fa1))

::> 114 commits in 13 version tags, last considered commit: af476092541e6e02f8ad1f94f93028a215f7fc25
