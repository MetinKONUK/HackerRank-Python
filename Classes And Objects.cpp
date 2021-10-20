// Write your Student class here
class Student {
    public:
    void input() {
    int a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;
    scores.push_back(a);
    scores.push_back(b);
    scores.push_back(c);
    scores.push_back(d);
    scores.push_back(e);
    }
    int calculateTotalScore(){
        int sum = 0;
        for(unsigned int i = 0; i < scores.size();i++) {
            sum += scores[i];
        }
        return sum;
    }
    private:
     vector<int> scores;
};
