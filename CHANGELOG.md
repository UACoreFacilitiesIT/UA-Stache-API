# Changelog

All notable changes to this project can be found here.
The format of this changelog is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

#### 2023/11/28[2.1.1](https://github.com/UACoreFacilitiesIT/UA-Stache-API)
Refactors env setup to use poetry.

#### 2020/02/01[2.1.0](https://github.com/UACoreFacilitiesIT/UA-Stache-API)
Added post method to ua stache api. Get entry now also accepts jsons that use 'X-STACHE-READ-KEY' or 'X-STACHE-KEY'. Auth method now contains a keyword get_all, which when set to True will return all available data on the entry, including nickname, purpose, etc...

#### 2021/1/20 [2.0.1](https://github.com/UACoreFacilitiesIT/UA-Stache-API/commit/cf85ecd59d7d47ab8b2b4f3f92c22640c896bca3)

Updated setup.py dependencies to be more explicit and contain every dependency.

- Previously some dependencies were not listed, but were assumed to be installed through other packages.

#### 2019/10/08[2.0.0](https://github.com/UACoreFacilitiesIT/UA-Stache-API/commit/c2179776f7f0c7f7044fa0ab891eaf5aa6235a4b)
In this new release, the get_entry method now takes a string, in the specified
format. The string that is given should be harvested from the same folder as the file that is running, so it can with open it.

#### 2019/10/03 [1.0.0](https://github.com/UACoreFacilitiesIT/UA-Stache-API/commit/41585c846c282beccb392736b61c98cfa0b4e727)
This is the initial start point for a University of Arizona Stache API.

- Moved repo from private repo to public.
