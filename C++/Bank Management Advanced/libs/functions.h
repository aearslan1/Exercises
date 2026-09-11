#include <iostream>
#include <string>
#include <vector>

namespace math{
    int min(int a, int b){
        if (a < b)
            return a;
        return b;
    }
    float min(float a, float b){
        if (a < b)
            return a;
        return b;
    }
}

namespace write{
    void n_write(int n, std::string text){
        for (int _ = 0; _ < n; _++){
            std::cout << text;
        }
    }

    void one_panel_string(std::string text){
        std::string formatted = " " + text + " ";
        int len = formatted.length();
        
        std::cout << "╔";
        n_write(len, "═");
        std::cout << "╗\n║" << formatted << "║\n╚";
        n_write(len, "═");
        std::cout << "╝\n";
    }

    void menu (std::string title, std::vector<std::string> list){
        write::one_panel_string(title);
        for (int i = 0; i < list.size(); i++){
            std::cout << "╚ " << i + 1 << "." << "[" << list[i] << "]" << "\n"; 
        }
    }

    void space(){
        std::cout << "\n\n" << "═════════════════════════" << "\n\n";
    }

    std::string input(std::string prompt){
        std::string value;

        one_panel_string(prompt);
        std::cout << "║" << "\n";
        std::cout << "╚> ";

        std::getline(std::cin, value);
        return value;
    }
}

namespace str{
    std::string n_string(int n, std::string text){
        std::string blank = "";
        for (int _ = 0; _ < n; _++){
            blank += text;
        }
        return blank;
    }
}

namespace boolean{
    std::string turn_string(bool statue){
        if (statue)
            return "True";
        
        else
            return "False";
    }
}

namespace flt{
    std::string low_float(std::string number){
        std::string blank = "";
        int number_lenght = number.length();
        int before_dot = 0;
        int after_dot = 0;
        bool dot_mode = false;
        for (int i = 0; i < number_lenght; i++){
            if (number[i] == '.'){
                dot_mode = true;
                continue;
            }
            
            if (dot_mode)
                after_dot += 1;
            
            else
                before_dot += 1;
        }

        if (before_dot > 6){
            for (char chr : number){
                if (chr == '.')
                    break;
                
                blank += chr;
            }
        }
        else{
            int read_lenght = math::min(6 - before_dot, after_dot) ; 

            for (int i = 0; i < before_dot; i++)
                blank += number[i];
            

            for (int i = 0; i < read_lenght; i++)
                blank += number[i + before_dot];
        }

        return blank;
    }
}