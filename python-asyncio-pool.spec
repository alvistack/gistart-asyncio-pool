# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-asyncio-pool
Epoch: 100
Version: 0.5.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Pool of asyncio coroutines with familiar interface
License: MIT
URL: https://github.com/gistart/asyncio-pool/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
AioPool makes sure no more and no less (if possible) than size spawned
coroutines are active at the same time. spawned means created and
scheduled with one of the pool interface methods, active means coroutine
function started executing it's code, as opposed to waiting -- which
waits for pool space without entering coroutine function.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-asyncio-pool
Summary: Pool of asyncio coroutines with familiar interface
Requires: python3
Provides: python3-asyncio-pool = %{epoch}:%{version}-%{release}
Provides: python3dist(asyncio-pool) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-asyncio-pool = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(asyncio-pool) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-asyncio-pool = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(asyncio-pool) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-asyncio-pool
AioPool makes sure no more and no less (if possible) than size spawned
coroutines are active at the same time. spawned means created and
scheduled with one of the pool interface methods, active means coroutine
function started executing it's code, as opposed to waiting -- which
waits for pool space without entering coroutine function.

%files -n python%{python3_version_nodots}-asyncio-pool
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-asyncio-pool
Summary: Pool of asyncio coroutines with familiar interface
Requires: python3
Provides: python3-asyncio-pool = %{epoch}:%{version}-%{release}
Provides: python3dist(asyncio-pool) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-asyncio-pool = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(asyncio-pool) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-asyncio-pool = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(asyncio-pool) = %{epoch}:%{version}-%{release}

%description -n python3-asyncio-pool
AioPool makes sure no more and no less (if possible) than size spawned
coroutines are active at the same time. spawned means created and
scheduled with one of the pool interface methods, active means coroutine
function started executing it's code, as opposed to waiting -- which
waits for pool space without entering coroutine function.

%files -n python3-asyncio-pool
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
