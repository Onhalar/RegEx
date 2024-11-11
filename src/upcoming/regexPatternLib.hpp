#include <string>
#include <map>
#include <regex>

using namespace std;

map<string, regex> patterns = {
    {"URL", regex("(https?:\\/\\/)?(www\\.)?([a-z0-9^\\s]+){1}(\\.[a-z]+){1}(\\/[^\\/\\s]+)*")}
};

