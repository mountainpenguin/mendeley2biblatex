"""
    \file mendeley2bibtex.py
    \author François Bianco, University of Geneva – francois.bianco@unige.ch
    \date 2012.09


    \mainpage Mendeley To BibTeX convertor

    This script converts Mendeley SQlite database to BibTeX file.


    \section Infos

     mendeley2bibtex.py was written by François Bianco, University of Geneva
– francois.bianco@unige.ch in order to get a correct conversion of Mendely
database to BibTeX not provided by the closed source Mendeley Desktop software.

    First locate your database. On Linux systems it is:

ls ~/.local/share/data/Mendeley\ Ltd./Mendeley\
Desktop/your@email.com@www.mendeley.com.sqlite

    Make a copy of this file, as we assume no responsability for loss of data.

    Then run mendeley2bibtex.py on your file with

        ./mendeley2bibtex.py -o mendeley.bib mendeley.sqlite


    \section Copyright

    Copyright © 2012 François Bianco, University of Geneva –
francois.bianco@unige.ch

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    See COPYING file for the full license.

    \section Updates

    2012.09:
        First Version

"""