Summary: PKCS#11 engine for OpenSSL
Name: engine_pkcs11
Version: 0.1.8
Release: 5
License: BSD
Group: System/Libraries
Source0: http://www.opensc-project.org/files/%{name}/%{name}-%{version}.tar.gz
Buildrequires: libp11-devel >= 0.2.1
Buildrequires: pkgconfig(openssl)
URL: https://www.opensc.org/engine_pkcs11

%description
Engine_pkcs11 is an implementation of an engine for OpenSSL. It can be loaded
using code, config file or command line and will pass any function call by
openssl to a PKCS#11 module. Engine_pkcs11 is meant to be used with smart cards
and software for using smart cards in PKCS#11 format, such as OpenSC. Originaly
this engine was a part of OpenSC, until OpenSC was split into several small
projects for improved flexibility.

%prep
%setup -q
cat > README.mandriva <<EOF
In Mandriva, the engine file has been placed in the
%{_libdir}/openssl/engines directory instead of the default
%{_libdir}/engines. This was done so in order to match our openssl
installation.

Considering this new path, below is the suggested change to openssl.cnf
in order to use this engine:

openssl_conf = openssl_def

[openssl_def]
engines = engine_section

[engine_section]
pkcs11 = pkcs11_section

[pkcs11_section]
engine_id = pkcs11
dynamic_path = %{_libdir}/openssl/engines/engine_pkcs11.so
MODULE_PATH = %{_libdir}/opensc-pkcs11.so
init = 0

EOF

chmod 0644 README.mandriva

%build
%configure2_5x --with-enginesdir=%{_libdir}/openssl/engines
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}%{_libdir}/openssl/engines/*.a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/README doc/nonpersistent/wiki.out/* README.mandriva
%{_libdir}/openssl/engines/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.8-3mdv2011.0
+ Revision: 610376
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 0.1.8-2mdv2010.1
+ Revision: 537454
- rebuild

* Thu Jan 07 2010 Frederik Himpe <fhimpe@mandriva.org> 0.1.8-1mdv2010.1
+ Revision: 487337
- update to new version 0.1.8

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.1.7-1mdv2010.1
+ Revision: 482764
- Update to new version 0.7.1
- a few cosmetic clean-ups in SPEC file

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.1.5-2mdv2010.0
+ Revision: 437462
- rebuild

* Tue Oct 14 2008 Funda Wang <fwang@mandriva.org> 0.1.5-1mdv2009.1
+ Revision: 293500
- new version 0.1.5

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1.4-3mdv2009.0
+ Revision: 244904
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 05 2007 Andreas Hasenack <andreas@mandriva.com> 0.1.4-1mdv2008.1
+ Revision: 106185
- updated to version 0.1.4


* Fri Jan 12 2007 Andreas Hasenack <andreas@mandriva.com> 0.1.3-3mdv2007.0
+ Revision: 107938
- rebuilt
- Import engine_pkcs11

* Mon Dec 05 2005 Andreas Hasenack <andreas@mandriva.com> 0.1.3-2mdk
- fix engine path to match openssl's
- added a README.mandriva file to explain this change

* Sat Dec 03 2005 Andreas Hasenack <andreas@mandriva.com> 0.1.3-1mdk
- packaged for Mandriva

