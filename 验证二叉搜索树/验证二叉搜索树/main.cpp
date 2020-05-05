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
    
    // pre表示前一个节点的4
    // 1判断当前的节点的值>pre
    // 2 判断当前节点的Left
    // 3 判断当前节点的right
    bool InOrder(TreeNode* root, long& pre) {
        
        if (root == nullptr) {
            return true;
        }
        
        if (!InOrder(root->left, pre)) {
            return false;
        }
        
        if (pre <= root->val) {
            return false;
        }
        
        pre = root->val;
        
        return InOrder(root->right, pre);
    }

    bool isValidBST(TreeNode* root) {
        
        long minLong = LONG_MIN;
        return InOrder(root, minLong);
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
