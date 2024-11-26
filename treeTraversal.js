class TreeNode {
    constructor(key) {
        this.key = key;
        this.left = null;   
        this.right = null;  
    }
}

class BinaryTree {
    constructor() {
        this.root = null;
    }

    insert(key) {
        if (this.root === null) {
            this.root = new TreeNode(key);
        } else {
            this._insertRecur(this.root, key);
        }
    }

    _insertRecur(node, key) {
        if (key < node.key) {
            if (node.left === null) {
                node.left = new TreeNode(key);
            } else {
                this._insertRecur(node.left, key);
            }
        } else if (key > node.key) {
            if (node.right === null) {
                node.right = new TreeNode(key);
            } else {
                this._insertRecur(node.right, key);
            }
        }
    }

    inOrderTrav() {
        let result = [];
        this._inOrderTravRecur(this.root, result);
        console.log(result.join(" "));
    }

    _inOrderTravRecur(node, result) {
        if (node) {
            this._inOrderTravRecur(node.left, result);
            result.push(node.key);
            this._inOrderTravRecur(node.right, result);
        }
    }

    preOrderTrav() {
        let result = [];
        this._preOrderTravRecur(this.root, result);
        console.log(result.join(" "));
    }

    _preOrderTravRecur(node, result) {
        if (node) {
            result.push(node.key);
            this._preOrderTravRecur(node.left, result);
            this._preOrderTravRecur(node.right, result);
        }
    }

    postOrderTrav() {
        let result = [];
        this._postOrderTravRecur(this.root, result);
        console.log(result.join(" "));
    }

    _postOrderTravRecur(node, result) {
        if (node) {
            this._postOrderTravRecur(node.left, result);
            this._postOrderTravRecur(node.right, result);
            result.push(node.key);
        }
    }

    logTree() {
        this._logTreeRecur(this.root, 0);
    }

    _logTreeRecur(node, depth) {
        if (node === null) {
            return;
        }
        this._logTreeRecur(node.right, depth + 1);
        console.log("   ".repeat(depth) + String(node.key));
        this._logTreeRecur(node.left, depth + 1)
    }
}

const tree = new BinaryTree();

// Insert keys
const keys = [50, 30, 70, 40, 20, 60, 80];
keys.forEach(key => tree.insert(key));

// In-order traversal
console.log('In-order traversal:');
tree.inOrderTrav();

// Pre-order traversal
console.log('Pre-order traversal:');
tree.preOrderTrav();


// Post-order traversal
console.log('Post-order traversal:');
tree.postOrderTrav();

// Log tree structure
console.log('Binary tree structure:');
tree.logTree();
