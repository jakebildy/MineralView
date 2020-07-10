paths = getArgument();
path = split(path,'#');

nameprefix = "tn"

function action (input, output, filename){
	open(input + filename);
	setThreshold(5, 5);
	run("Convert to Mask");
	saveAs("tiff",output + nameprefix + filename);
	run("Analyze Particles...", "size=100-Infinity display exclude clear add");
	dotIndex = indexOf(filename, "."); 
    title = substring(filename, 0, dotIndex);
	
	saveAs("Results",output + nameprefix +title + ".csv");
}

setBatchMode(true); 
list = getFileList(path[0]);
for (i = 0; i < list.length; i++)
        action(path[0], path[1], list[i]);
setBatchMode(false);
