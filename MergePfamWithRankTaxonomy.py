#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:16:20 2018

@author: ericsalomaki
"""

import pandas as pd


TaxID_and_RankTax=pd.read_table("/Users/ericsalomaki/Desktop/AcetylCoA_Evolution/Pfam/PhyFamSpTaxID.txt", header=None, sep='\t')
Acc_and_TaxID=pd.read_table("/Users/ericsalomaki/Desktop/AcetylCoA_Evolution/Pfam/Accessions_TaxIDs.txt", header=None, sep='\t')
Pfam_Domains=pd.read_table("/Users/ericsalomaki/Desktop/AcetylCoA_Evolution/Pfam/AllThreeDomains.Pfam.FoundDomainsNoAccDecimal.tsv", header=None, sep='\t')

TaxID_and_RankTax.columns=["Phylum","Family","Species","TaxID"]
Acc_and_TaxID.columns=["Accession","TaxID"]
Pfam_Domains.columns=["Domain","PfamAcc","Accession","Evalue","Score","Start","End"]


Acc_TaxID_RankTax=Acc_and_TaxID.merge(TaxID_and_RankTax,on="TaxID", how="inner")
Pfam_Domains_With_Taxonomy=Pfam_Domains.merge(Acc_TaxID_RankTax,on="Accession", how="left")
Pfam_Domains_With_Taxonomy.drop_duplicates(subset=None,keep='first', inplace=True)
Pfam_Domains_With_Taxonomy.to_csv("/Users/ericsalomaki/Desktop/AcetylCoA_Evolution/Pfam/Pfam_Domains_With_Taxonomy.tsv", sep='\t', index=False)
