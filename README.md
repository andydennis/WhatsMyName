# WhatsMyNamePackage
This repository has the unified data required to perform user and username enumeration on various websites. Content is in a JSON file and can easily be used in other projects such as the ones below:

![whatsmyname](whatsmyname.png)

[![Open Source](https://img.shields.io/badge/Open%20Source-100%25-green.svg)](https://shields.io/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green.svg)](https://github.com/GetStream/winds/graphs/commit-activity)
[![Version](https://img.shields.io/badge/Version-2.0-orange)](https://github.com/GetStream/winds/graphs/commit-activity)

* https://whatsmyname.app/ - [Chris Poulter](https://twitter.com/osintcombine) created this site which draws the project's JSON file into a gorgeous and easy to use web interface.
  * There are no ads.
  * He does not collect what you search for
  * Filters for category and in search results
  * FAST!
  * Pulls the lastest version of the project's JSON file when run.
* [Recon-ng](https://bitbucket.org/LaNMaSteR53/recon-ng) - The [Profiler Module](https://bitbucket.org/LaNMaSteR53/recon-ng/src/7723096ce2301092906838ef73564e7907886748/modules/recon/profiles-profiles/profiler.py?at=master&fileviewer=file-view-default) grabs this JSON file and uses it. See https://webbreacher.com/2014/12/11/recon-ng-profiler-module/ for details.
* [Spiderfoot](https://github.com/smicallef/spiderfoot) uses this in the [sfp_account](https://github.com/smicallef/spiderfoot/blob/master/modules/sfp_accounts.py) module. There is also [this video](https://asciinema.org/a/295923) showing how to use this project using the Spiderfoot Command Line Interface (CLI).
* [sn0int](https://github.com/kpcyrd/sn0int) downloads and uses the JSON file in the [kpcyrd/whatsmyname](https://sn0int.com/r/kpcyrd/whatsmyname) module, see https://twitter.com/sn0int/status/1228046880459907073 for details and instructions.

## Installation

The code can be installed by cloning the repository and installing via pip. Use pip3 for the latest version.

```
pip3 install -e WhatsMyName
```


## Format
The format of the JSON is simple. There are 3 main elements:

1. License - The license for this project and its data
2. Authors - The people that have contributed to this project
3. Sites - This is the main data

Within the "sites" elements, the format is as follows (with several parameters being optional):

```json
     ...
      {
         "name" : "name of the site",
         "check_uri" : "URI to check the site with the {account} string replaced by a username",
         "pretty_uri" : "if the check_uri is for an API, this OPTIONAL element can show a human-readable page",
         "account_existence_code" : "the HTTP response code for a good 'account is there' response",
         "account_existence_string" : "the string in the response that we look for for a good response",
         "account_missing_string" : "this OPTIONAL string will only be in the response if there is no account found ",
         "account_missing_code" : "the HTTP response code for a bad 'account is not there' response",
         "known_accounts" : ["a list of user accounts that can be used to test","for user enumeration"],
         "allowed_types" : ["these are the types of data and categories of the content"],
         "category" : "a category for what the site is mainly used for",
         "valid" : "this true or false boolean field is used to enable or disable this site element",
         "comments" : ["a list of comments including when this was last verified and outcomes"]
      },
      ...
```

Here is an example of a site element:

```json
     ...
      {
         "name" : "GitHub",
         "check_uri" : "https://api.github.com/users/{account}",
         "pretty_uri" : "https://github.com/{account}",
         "account_existence_code" : "200",
         "account_existence_string" : "login:",
         "account_missing_string" : ["Not Found"],
         "account_missing_code" : "404",
         "known_accounts" : ["test","webbreacher"],
         "allowed_types" : ["String","Person","WebAccount","Username","Organization"],
         "category" : "coding",
         "valid" : true,
         "comments" : ["verified 11/08/2015 - webbreacher"]
      },
      ...
```

## Standalone Checker
If you just want to run this script to check user names on sites and don't wish to use it in combination with another tool (like Recon-NG and/or Spiderfoot), then you can use the included Python script as shown below:

```
 $  python3 -m whats_my_name -u username
Running
 -  253 sites found in file.
 -  Looking up https://www.7cups.com/@username
[+] Found user at https://www.7cups.com/@username
 -  Looking up https://asciinema.org/~username
[+] Found user at https://asciinema.org/~username
 -  Looking up https://audiojungle.net/user/username
[+] Found user at https://audiojungle.net/user/username
 -  Looking up https://www.biggerpockets.com/users/username
[+] Found user at https://www.biggerpockets.com/users/username
 -  Looking up https://www.bookcrossing.com/mybookshelf/username
[+] Found user at https://www.bookcrossing.com/mybookshelf/username
 -  Looking up https://www.buymeacoffee.com/username
[+] Found user at https://www.buymeacoffee.com/username
 -  Looking up https://www.championat.com/user/username/
      !  ERROR: BAD CODE AND STRING. Neither the HTTP response code or detection string worked.
 -  Looking up https://community.cloudflare.com/u/username
      !  ERROR: BAD CODE AND STRING. Neither the HTTP response code or detection string worked.
 -  Looking up https://www.cnet.com/profiles/username/
...
[+] Found user at https://vero.co/username
 -  Looking up https://www.tiktok.com/@username?lang=en
      !  ERROR: BAD DETECTION STRING. "s Newest TikTok Videos</title>" was not found on resulting page.
 -  Looking up https://mixi.jp/view_community.pl?id=username
      !  ERROR: BAD DETECTION STRING. "| mixiコミュニティ</title>" was not found on resulting page.
 -  Looking up https://www.blogger.com/profile/username
      !  ERROR: BAD CODE AND STRING. Neither the HTTP response code or detection string worked.
 -  Looking up https://armorgames.com/user/username
[+] Found user at https://armorgames.com/user/username
Finished
```

## Updates
I update this project as I have time and would *LOVE* to have interested people help maintain and grow it. 
Please reach to me webbreacher {at} gmail {dot} com if you are interested.

## Contributors
[@WebBreacher](https://github.com/WebBreacher/)<br>
[@Munchko](https://github.com/Munchko/)<br>
[@L0r3m1p5um](https://github.com/L0r3m1p5um/)<br>
[@lehuff](https://github.com/lehuff/)<br>
[@arnydo](https://github.com/arnydo)<br>
[@janbinx](https://github.com/janbinx/)<br>
[@bcoles](https://github.com/bcoles)<br>
[@Sector035](https://github.com/sector035/)<br>
[@mccartney](https://github.com/mccartney)<br>
[@salaheldinaz](https://github.com/salaheldinaz)<br>
[@rpigu-i](https://github.com/rpigu-i/)<br>
