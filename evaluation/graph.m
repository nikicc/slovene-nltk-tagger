%data
fractions = [0.75, 0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99 ];
TrigramTagger = [0.828648, 0.830353, 0.830551, 0.829855, 0.830609, 0.829901, 0.828807, 0.827759, 0.827613, 0.828121, 0.827826, 0.828913, 0.838798, 0.840060, 0.841683, 0.837875];
BrillTagger = [0.849031, 0.851387, 0.851527, 0.850839, 0.851240, 0.851680, 0.850737, 0.848899, 0.848964,  0.849090, 0.849636, 0.851041, 0.860899, 0.861213, 0.862869, 0.857844];
NaiveBayes = [0.845122, 0.846063, 0.846490, 0.846221, 0.847159, 0.847387, 0.846713, 0.846211, 0.846384, 0.846358, 0.846064, 0.847508, 0.853809, 0.856799, 0.858779 , 0.856699];

%plot
figure(1);clf; hold on; grid on ;
set(gca,'fontsize',10); % sets font of numbers on axes
plot(fractions, BrillTagger,'g-o');
plot(fractions, NaiveBayes,'b-o');
plot(fractions, TrigramTagger,'r-o');

xlabel ('Fraction of exmaples, used for learning');
ylabel ('Accuracy');
legend ('BrillTagger','NaiveBayes','TrigramTagger');

fprintf('Average accuracy BrillTagger %g.\n',mean(BrillTagger))
fprintf('Average accuracy NaiveBayes %g.\n',mean(NaiveBayes))
fprintf('Average accuracy TrigramTagger %g.\n',mean(TrigramTagger))
