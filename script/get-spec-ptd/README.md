Automatically generated README for this automation recipe: **get-spec-ptd**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-spec-ptd,7423a878e4524136) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-spec-ptd)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,spec,ptd,ptdaemon,power,daemon,power-daemon,mlperf,mlcommons*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,spec,ptd,ptdaemon,power,daemon,power-daemon,mlperf,mlcommons`

`cm run script --tags=get,spec,ptd,ptdaemon,power,daemon,power-daemon,mlperf,mlcommons [--input_flags]`

*or*

`cmr "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons"`

`cmr "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons " [--input_flags]`



#### Input Flags

* --**input**=Path to SPEC PTDaemon (Optional)

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```
#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,spec,ptd,ptdaemon,power,daemon,power-daemon,mlperf,mlcommons'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="get,spec,ptd,ptdaemon,power,daemon,power-daemon,mlperf,mlcommons"```

#### Run this script via Docker (beta)

`cm docker script "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--input=value`  &rarr;  `CM_INPUT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_CHECKOUT: `main`
* CM_GIT_DEPTH: `--depth 1`
* CM_GIT_PATCH: `no`
* CM_GIT_RECURSE_SUBMODULES: ` `
* CM_GIT_URL: `https://github.com/mlcommons/power.git`

</details>

#### Versions
Default version: `main`

* `custom`
* `main`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-spec-ptd/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/cm4mlops/tree/master/script/detect-os)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/cm4mlops/tree/master/script/get-python3)
     * get,git,repo,_repo.https://github.com/mlcommons/power
       - CM script: [get-git-repo](https://github.com/mlcommons/cm4mlops/tree/master/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-spec-ptd/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-spec-ptd/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-spec-ptd/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-spec-ptd/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-spec-ptd/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-spec-ptd/_cm.json)

___
### Script output
`cmr "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons " [--input_flags] -j`
#### New environment keys (filter)

* `CM_MLPERF_PTD_PATH`
* `CM_SPEC_PTD_PATH`
#### New environment keys auto-detected from customize

* `CM_MLPERF_PTD_PATH`
* `CM_SPEC_PTD_PATH`