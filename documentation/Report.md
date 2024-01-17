A report is to be dependent on a patient and the genes of the patient that have been selected for the specific report generation.

It will be generated as a Word document (docx) and will have the following look:

```
Objective 1
	Category of Gene
		* Set of Advice
		(gene)
		* Set of Advice
		(gene)
	Category of Gene
		* Set of Advice
		(gene)
Objective 2
	Category of Gene
		* Set of Advice
		(gene)
		* Set of Advice
		(gene)
	Category of Gene
		* Set of Advice
		(gene)
....
```

A typical use case of the report is as follows:

```
report = patient.create_report()
report.generate_pdf()
```
