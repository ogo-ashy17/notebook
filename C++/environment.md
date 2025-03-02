**Create Environment C++**

**1. Install gcc**

Last login: Thu Feb 20 22:49:40 on ttys000
dgmr2@shougonoMacBook-Air ~ % brew list | grep gcc
dgmr2@shougonoMacBook-Air ~ % brew install gcc
==> Auto-updating Homebrew...
Adjust how often this is run with HOMEBREW_AUTO_UPDATE_SECS or disable with
HOMEBREW_NO_AUTO_UPDATE. Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Auto-updated Homebrew!
Updated 4 taps (azure/functions, homebrew/services, homebrew/core and homebrew/cask).
==> New Formulae
ad                         git-mob                    ramalama
adapterremoval             globstar                   ratarmount
aqua                       go@1.23                    rattler-index
arelo                      gomi                       reuse
bacon-ls                   gowall                     rink
bagels                     havener                    ruby-lsp
bazel@7                    hcledit                    rustic
bombardier                 hishtory                   rustywind
bpmnlint                   hk                         sby
cf-terraforming            hl                         sitefetch
cfnctl                     identme                    snowflake-cli
cloudfoundry-cli           infisical                  soft-serve
code2prompt                jira-cli                   sql-formatter
comrak                     jsrepo                     sv2v
cot                        jupytext                   symfony-cli
cspell                     keeper-commander           taskflow
dbg-macro                  kirimase                   text-embeddings-inference
dockerfilegraph            koji                       tgpt
dtsroll                    lazyjj                     threatcl
dyff                       libpostal                  vfkit
evil-helix                 libpostal-rest             visidata
exomizer                   mac                        vscli
fancy-cat                  md2pdf                     wfa2-lib
fastly                     mdq                        xk6
feluda                     mummer                     yamlfix
flow-control               nak                        yices2
foundry                    nping                      yoke
fricas                     nuitka                     yor
garnet                     pdfly                      zimfw
gauth                      pkl-lsp                    zlib-ng-compat
ggh                        postgresql-hll             zns
==> New Casks
autogram                                 jumpcloud-password-manager
automounterhelper                        kunkun
badgeify                                 losslessswitcher
batfi                                    luanti
block-goose                              mitti
browser-actions                          obscura-vpn
candy-crisis                             open-eid
chatwise                                 opera-air
cherry-studio                            oracle-jdk-javadoc@21
font-aporetic                            pairpods
font-big-shoulders                       pdl
font-big-shoulders-inline                pinwheel
font-big-shoulders-stencil               precize
font-boldonse                            structuredlogviewer
font-bytesized                           thumbhost3mf
font-comic-relief                        trae
font-sf-mono-nerd-font-ligaturized       ui-tars
fuse-t                                   veracrypt-fuse-t
gologin                                  vernier-spectral-analysis
granola                                  vezer
istatistica-core                         windsurf@next

You have 27 outdated formulae installed.

==> Downloading https://ghcr.io/v2/homebrew/core/gcc/manifests/14.2.0_1
######################################################################### 100.0%
==> Fetching dependencies for gcc: gmp, isl, mpfr and libmpc
==> Downloading https://ghcr.io/v2/homebrew/core/gmp/manifests/6.3.0
######################################################################### 100.0%
==> Fetching gmp
==> Downloading https://ghcr.io/v2/homebrew/core/gmp/blobs/sha256:6683d73d6677d2
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/isl/manifests/0.27
######################################################################### 100.0%
==> Fetching isl
==> Downloading https://ghcr.io/v2/homebrew/core/isl/blobs/sha256:de143fddb0e20b
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/mpfr/manifests/4.2.1
######################################################################### 100.0%
==> Fetching mpfr
==> Downloading https://ghcr.io/v2/homebrew/core/mpfr/blobs/sha256:51f0ca19e8977
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libmpc/manifests/1.3.1
######################################################################### 100.0%
==> Fetching libmpc
==> Downloading https://ghcr.io/v2/homebrew/core/libmpc/blobs/sha256:5c8cdc4d460
######################################################################### 100.0%
==> Fetching gcc
==> Downloading https://ghcr.io/v2/homebrew/core/gcc/blobs/sha256:96d8bf02f621cf
######################################################################### 100.0%
==> Installing dependencies for gcc: gmp, isl, mpfr and libmpc
==> Installing gcc dependency: gmp
==> Downloading https://ghcr.io/v2/homebrew/core/gmp/manifests/6.3.0
Already downloaded: /Users/dgmr2/Library/Caches/Homebrew/downloads/70a72a71216843d66a953c06ff6337445ce9bc94fae9f0e301e2f59005274a8e--gmp-6.3.0.bottle_manifest.json
==> Pouring gmp--6.3.0.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/gmp/6.3.0: 22 files, 3.3MB
==> Installing gcc dependency: isl
==> Downloading https://ghcr.io/v2/homebrew/core/isl/manifests/0.27
Already downloaded: /Users/dgmr2/Library/Caches/Homebrew/downloads/40b1c5526f95db33208143fa79887179e758121659d8877597f553e6e6188879--isl-0.27.bottle_manifest.json
==> Pouring isl--0.27.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/isl/0.27: 74 files, 7.6MB
==> Installing gcc dependency: mpfr
==> Downloading https://ghcr.io/v2/homebrew/core/mpfr/manifests/4.2.1
Already downloaded: /Users/dgmr2/Library/Caches/Homebrew/downloads/a2a3424f4974f6febfa0334a93f35f508eaef3f4ad04320f73d9498302295635--mpfr-4.2.1.bottle_manifest.json
==> Pouring mpfr--4.2.1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/mpfr/4.2.1: 31 files, 3MB
==> Installing gcc dependency: libmpc
==> Downloading https://ghcr.io/v2/homebrew/core/libmpc/manifests/1.3.1
Already downloaded: /Users/dgmr2/Library/Caches/Homebrew/downloads/fdfa98e0f8bb3ce075cb32776ac2345aa2f89252706c162aecfc841085fa76be--libmpc-1.3.1.bottle_manifest.json
==> Pouring libmpc--1.3.1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libmpc/1.3.1: 13 files, 492.3KB
==> Installing gcc
==> Pouring gcc--14.2.0_1.arm64_sequoia.bottle.tar.gz
==> Downloading https://formulae.brew.sh/api/formula.jws.json
🍺  /opt/homebrew/Cellar/gcc/14.2.0_1: 1,914 files, 459.8MB
==> Running `brew cleanup gcc`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
dgmr2@shougonoMacBook-Air ~ % brew list | grep gcc
gcc
dgmr2@shougonoMacBook-Air ~ % ls /usr/local/bin 
R				docker-credential-ecr-login
Rscript				docker-credential-osxkeychain
com.docker.cli			docker-index
docker				hub-tool
docker-compose			kubectl
docker-credential-desktop	kubectl.docker
dgmr2@shougonoMacBook-Air ~ % gcc -V
clang: error: argument to '-V' is missing (expected 1 value)
clang: error: no input files
dgmr2@shougonoMacBook-Air ~ % ls -l /usr/local/bin | grep g++
dgmr2@shougonoMacBook-Air ~ % ls
Applications		Movies			kaggle
Desktop			Music			notebook
Documents		Pictures		poetry-demo
Downloads		Public			teststreamlit
Library			docker-intro
Machine-Learning	docker-python
dgmr2@shougonoMacBook-Air ~ % cd notebook
dgmr2@shougonoMacBook-Air notebook % cd C++     
dgmr2@shougonoMacBook-Air C++ % vi test.cpp
dgmr2@shougonoMacBook-Air C++ % ls
environment.md	test.cpp
dgmr2@shougonoMacBook-Air C++ % g++-14 test.cpp
Undefined symbols for architecture arm64:
  "_main", referenced from:
      <initial-undefines>
ld: symbol(s) not found for architecture arm64
collect2: error: ld returned 1 exit status
dgmr2@shougonoMacBook-Air C++ % ls
environment.md	test.cpp
dgmr2@shougonoMacBook-Air C++ % which gcc-14
/opt/homebrew/bin/gcc-14
dgmr2@shougonoMacBook-Air C++ % which g++14
g++14 not found
dgmr2@shougonoMacBook-Air C++ % which g++-14
/opt/homebrew/bin/g++-14
dgmr2@shougonoMacBook-Air C++ % ls /usr/local/bin  
R				docker-credential-ecr-login
Rscript				docker-credential-osxkeychain
com.docker.cli			docker-index
docker				hub-tool
docker-compose			kubectl
docker-credential-desktop	kubectl.docker
dgmr2@shougonoMacBook-Air C++ % 

dgmr2@shougonoMacBook-Air bin % sudo ln -s ../../../opt/homebrew/bin/gcc-14 /usr/local/bin/gcc
Password:
dgmr2@shougonoMacBook-Air bin % ls
R				docker				docker-credential-ecr-login	gcc				kubectl.docker
Rscript				docker-compose			docker-credential-osxkeychain	hub-tool
com.docker.cli			docker-credential-desktop	docker-index			kubectl
dgmr2@shougonoMacBook-Air bin % sudo ln -s ../../../opt/homebrew/bin/g++-14 /usr/local/bin/g++
dgmr2@shougonoMacBook-Air bin % ls
R				docker				docker-credential-ecr-login	g++				kubectl
Rscript				docker-compose			docker-credential-osxkeychain	gcc				kubectl.docker
com.docker.cli			docker-credential-desktop	docker-index			hub-tool
dgmr2@shougonoMacBook-Air bin % which gcc 
/usr/bin/gcc
dgmr2@shougonoMacBook-Air bin % which g++
/usr/bin/g++
dgmr2@shougonoMacBook-Air bin % gcc --version
Apple clang version 16.0.0 (clang-1600.0.26.6)
Target: arm64-apple-darwin24.3.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin
dgmr2@shougonoMacBook-Air bin % g++ --version
Apple clang version 16.0.0 (clang-1600.0.26.6)
Target: arm64-apple-darwin24.3.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin
dgmr2@shougonoMacBook-Air bin % 
dgmr2@shougonoMacBook-Air ~ % which gcc
/usr/bin/gcc
dgmr2@shougonoMacBook-Air ~ % which gcc-14
/opt/homebrew/bin/gcc-14
dgmr2@shougonoMacBook-Air ~ % source ~/.zshrc
dgmr2@shougonoMacBook-Air ~ % echo $PATH
/Users/dgmr2/.pyenv/shims:/Users/dgmr2/.pyenv/bin:/opt/homebrew/bin:/Users/dgmr2/.pyenv/bin:/opt/homebrew/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Library/TeX/texbin
dgmr2@shougonoMacBook-Air ~ % g++ -V    
g++: error: unrecognized command-line option '-V'
g++: fatal error: no input files
compilation terminated.
dgmr2@shougonoMacBook-Air ~ % g++ --version
g++ (Homebrew GCC 14.2.0_1) 14.2.0
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

dgmr2@shougonoMacBook-Air ~ % gcc --version
gcc (Homebrew GCC 14.2.0_1) 14.2.0
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

dgmr2@shougonoMacBook-Air ~ % 
