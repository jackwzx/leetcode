//
//  main.cpp
//  验证二叉搜索树
//
//  Created by jackwangliang on 2020/5/5.
//  Copyright © 2020 jackwangliang. All rights reserved.
//

#include <iostream>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    bool InOrder(TreeNode* root, long& pre) {
        if (root == NULL) {
            return true;
        }
        if (!InOrder(root->left, pre)) {
            return false;
        }
        if (root->val <= pre) {
            return false;
        }
        pre = root->val;
        return InOrder(root->right, pre);
    }

    bool isValidBST(TreeNode* root) {
        long pre = LONG_MIN;
        return InOrder(root, pre);
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
