Simply demo for Atlas - a database of genetic variation in bateria.  

# Usage

Add new variants to atlas

./add-new-variants-to-database.py sample.vcf --db_name :db_name --kmer :kmer_size

# AMR prediction

atlas amr -s C00003204 -1 C00003204.bam

# Make panels

./bin/make-variant-panel.py -f staph-panel.txt -g data/BX571856.1.gb data/BX571856.1.fasta
time ./bin/make-variant-panel.py -f TBFullPanel.txt -g data/NC_000962.3.gb data/NC_000962.3.fasta > tb-amr-probes.fasta

# Dump variant probes

./main.py dump-probes data/NC_000962.3.fasta > panel_tb_k31.fasta

# Genotype using these variants

./main.py genotype panel_tb_k31.fasta 31 -s 10564-01 -1 /data2/users/phelim/data/tb/atlas/fastq/10564-01/10564-01.fastq.gz

./main.py genotype tb-amr-probes.fasta 31 -s 10564-01 -1 /data2/users/phelim/data/tb/atlas/fastq/10564-01/10564-01.fastq.gz

