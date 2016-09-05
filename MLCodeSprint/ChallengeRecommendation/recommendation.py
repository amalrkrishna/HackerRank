import pandas as pd
import operator
import json

def main():
	dfc = pd.read_csv('challenges.csv')
	dfs = pd.read_csv('submissions.csv')
	
	id = dfs.hacker_id.unique()
	contest = dfc.challenge_id.unique()
	
	arr = {}
	for i in contest:
		arr[i] = {}
	
	dp = 0
	if dp == 0:
		for i in id:
			temp = dfs['challenge_id'][dfs['hacker_id']==i].unique()
			for j in temp:
				for k in temp:
					print i, j, k
					if j != k:
						if k in arr[j]:
							arr[j][k] += 1
						else:
							arr[j][k] = 1
						if j in arr[k]:
							arr[k][j] += 1
						else:
							arr[k][j] = 1
		with open('temp.json','w') as f:
			json.dump(arr,f)
	else:
		with open('temp.json') as f:
			arr = json.load(f)

	con = dfc.contest_id.unique()
	array = {}
	for i in con:
		temp = dfc['challenge_id'][dfc['contest_id']==i].values
		temp1 = dfc['difficulty'][dfc['contest_id']==i].values
		y = []
		for iii in xrange(len(temp)):
			y.append((temp[iii],temp1[iii]))
		array[i] = y
		
	difficulty = {}
	for i in contest:
		difficulty[i] = dfc['difficulty'][dfc['challenge_id'] == i].values[0]
	
	df = dfc.sort('total_submissions_count', ascending=False).head(100)
	common = df['challenge_id'].values
	
	output = []
	for i in id:
		tt = [i]
		temp = dfs[dfs['hacker_id']==i]
		temp1 = temp['challenge_id'].unique()
		temp2 = temp['challenge_id'].values
		temp3 = temp['solved'].values
		temp4 = temp['contest_id'].unique()
		solved = []
		notSolved = []
		solve,noSolve = 0,0
		ns,nns = 0,0
		for k in xrange(len(temp1)):
			temp_k = [temp3[xx] for xx in xrange(len(temp3)) if temp2[xx] == temp1[k]]
			if 1 in temp_k:
				solved.append(temp1[k])
				ns += 1
				solve += difficulty[temp1[k]]
			else:
				notSolved.append(temp1[k])
				nns += 1
				noSolve += difficulty[temp1[k]]
		if ns > 0:
			solve /= ns
			solve -= 0.095
		if nns > 0:
			noSolve /= nns
			noSolve += 0.095
		
		for yy in notSolved:
			if difficulty[yy] <= noSolve-0.095:
				tt.append(yy)
		
		candidate = {}
		for j in temp1:
			t = sorted(arr[j].items(), key=operator.itemgetter(1), reverse=True)
			for ii in t:
				if ii[0] not in candidate:
					candidate[ii[0]] = ii[1]
		t = sorted(candidate.items(), key=operator.itemgetter(1), reverse=True)
		for jj in t:
			if jj[0] not in solved and jj[0] not in tt:
				if solve != 0 and noSolve != 0:
					if difficulty[jj[0]] >= solve or difficulty[jj[0]] <= noSolve:
						tt.append(jj[0])
				elif solve == 0:
					if difficulty[jj[0]] <= noSolve:
						tt.append(jj[0])
				else:
					if difficulty[jj[0]] >= solve:
						tt.append(jj[0])
			if len(tt) >= 11:
				break
		if len(tt) < 11:
			print i
			print tt
			for kk in temp4:
				temp_ = array[kk]
				if solve != 0 and noSolve != 0:
					tt += [temp_[a][0] for a in xrange(len(temp_)) if (temp_[a][1] <= noSolve or temp_[a][1] >= solve) and temp_[a][0] not in tt and temp_[a][0] not in solved]
				elif solve == 0:
					tt += [temp_[a][0] for a in xrange(len(temp_)) if temp_[a][1] <= noSolve and temp_[a][0] not in tt and temp_[a][0] not in solved]
				else:
					tt += [temp_[a][0] for a in xrange(len(temp_)) if temp_[a][1] >= solve and temp_[a][0] not in tt and temp_[a][0] not in solved]
			if len(tt) < 11:
				for to in common:
					if to not in solved and to not in tt:
						if solve != 0 and noSolve != 0:
							if difficulty[to] >= solve or difficulty[to] <= noSolve:
								tt.append(to)
						elif solve == 0:
							if difficulty[to] <= noSolve:
								tt.append(to)
						else:
							if difficulty[to] >= solve:
								tt.append(to)
					if len(tt) == 11:
						break
		elif len(tt) > 11:
			print i
			print tt
		tt = tt[:11]
		output.append(tt)
	
	output_file = open('recommendation.csv','wb')
	for i in output:
		output_file.write(','.join(i)+'\r\n')

if __name__ == '__main__':
	main()
