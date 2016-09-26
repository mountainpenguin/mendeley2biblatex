#!/usr/bin/env python

import os
import pandas as pd

class MedLine:
    def __init__(self):
        if os.path.exists(self._t("medline.pandas")):
            self.medline = self.get_store()
        else:
            self.medline = self.parse_medline()

    def _t(self, x):
        target = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            x
        )
        return target

    def get_ital(self, title):
        if os.path.exists("../../italics.txt"):
            ital_file = open("../../italics.txt").read().split("\n")[:-1]
            for i in ital_file:
                if i in title:
                    title = title.replace(i, "\\textit{%s}" % i)
        return title

    def get_abbr(self, journal, issn):
        if not journal and not issn:
            return journal
        journal_q = journal.lower()
        # select by issn
        if issn:
            query = (
                ((self.medline["ISSN (Print)"] == issn) |
                 (self.medline["ISSN (Online)"] == issn) |
                 (self.medline["JournalTitle"] == journal_q))
            )

        else:
            query = (
                self.medline["JournalTitle"] == journal_q
            )
        search = self.medline[query]
        if len(search) == 1:
            abbr = search.IsoAbbr.iloc[0]
            return abbr
        elif len(search) > 1:
            search2 = search[(search["ISSN (Print)"] != "") | (search["ISSN (Online)"] != "")]
            if len(search2) >= 1:
                abbr = search2.IsoAbbr.iloc[0]
                return abbr
            else:
                return search.IsoAddr.iloc[0]
        else:
            return journal

    def parse_medline(self):
        input_file = open(self._t("J_Medline.txt")).read()
        entries = input_file.split("-" * 56)[1:]
        wanted_keys = [
            "JournalTitle", "MedAbbr",
            "ISSN (Print)", "ISSN (Online)",
            "IsoAbbr"
        ]
        outdata = pd.DataFrame(columns=wanted_keys)

        for e in entries:
            e = e.strip()
            e_data = {}
            for line in e.split("\n"):
                key = line.split(": ")[0]
                value = ": ".join(line.split(": ")[1:])
                if key in wanted_keys:
                    if key == "JournalTitle":
                        e_data[key] = value.lower()
                    else:
                        e_data[key] = value
            outdata = outdata.append(pd.Series(e_data), ignore_index=True)

        outdata.to_pickle(self._t("medline.pandas"))
        return outdata

    def get_store(self):
        return pd.read_pickle(self._t("medline.pandas"))


if __name__ == "__main__":
    m = MedLine()
