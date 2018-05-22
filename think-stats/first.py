from __future__ import division
import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)
live_births = []
first_births = []
other_births = []

for recode in table.records:
    if recode.outcome is 1:
        live_births.append(recode)
        if recode.birthord is 1:
            first_births.append(recode)
        else:
            other_births.append(recode)
print 'live births:', len(live_births)
print 'first births:', len(first_births)
print 'other births:', len(other_births)


def mean(arr):
    return sum([record.prglength for record in arr]) / len(arr)


mean_first_births = mean(first_births)
mean_other_births = mean(other_births)
print 'avg pregnancy length for first babies:', mean_first_births
print 'avg pregnancy length for other babies:', mean_other_births
print 'difference:', mean_first_births - mean_other_births
