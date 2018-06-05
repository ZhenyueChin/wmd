from subprocess import call

call(['python2', 'get_word_vectors.py', 'all_twitter_by_line.txt', 'twitter_vec.pk', 'twitter_vec.mat'])
call(['python2', 'wmd.py', 'twitter_vec.pk', 'twitter_wmd_d.pk'])

